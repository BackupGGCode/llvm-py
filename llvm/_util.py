# 
# Copyright (c) 2008, Mahadevan R All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
#  * Neither the name of this software, nor the names of its 
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 

"""Utility functions and classes.

Used only in other modules, not for public use."""

import llvm
import llvm._core as _core  # for PyCObjectVoidPtrToPyLong
from weakref import WeakValueDictionary


#===----------------------------------------------------------------------===
# A set of helpers to check various things. Raises exceptions on
# failures.
#===----------------------------------------------------------------------===

def check_gen(obj, type):
    if not isinstance(obj, type):
        type_str = type.__name__
        msg = "argument not an instance of llvm.core.%s" % type_str
        raise TypeError, msg

def check_is_unowned(ownable):
    if ownable.owner:
        raise llvm.LLVMException, "object is already owned"


#===----------------------------------------------------------------------===
# A set of helpers to unpack a list of Python wrapper objects
# into a list of PyCObject wrapped objects, checking types along
# the way.
#===----------------------------------------------------------------------===

def unpack_gen(objlist, check_fn):
    for obj in objlist: check_fn(obj)
    return [ obj.ptr for obj in objlist ]


#===----------------------------------------------------------------------===
# Helper to wrap over iterables (LLVMFirstXXX, LLVMNextXXX). This used
# to be a generator, but that loses subscriptability of the result, so
# we now return a list.
#===----------------------------------------------------------------------===

def wrapiter(first, next, container, wrapper, extra=[]):
#    ptr = first(container)
#    while ptr:
#        yield wrapper(ptr)
#        ptr = next(ptr)
    ret = []
    ptr = first(container)
    while ptr:
        ret.append(wrapper(ptr, *extra))
        ptr = next(ptr)
    return ret


#===----------------------------------------------------------------------===
# Dummy owner, will not delete ownee. Be careful.
#===----------------------------------------------------------------------===

class dummy_owner(object):

    def __init__(self, ownee):
        ownee._own(self)


#===----------------------------------------------------------------------===
# A metaclass to prevent aliasing.  It stores a (weak) reference to objects
# constructed based on a PyCObject.  If an object is constructed based on a
# PyCObject with the same underlying pointer as a previous object, a reference
# to the previous object is returned rather than a new one.
#===----------------------------------------------------------------------===

class ObjectCache(type):
    """A metaclass to prevent aliasing.

    Classes using 'ObjectCache' as a metaclass must have constructors
    that take a PyCObject as their first argument.  When the class is
    called (to create a new instance of the class), the value of the
    pointer wrapped by the PyCObj is checked:

        If no previous object has been created based on the same
        underlying pointer (note that different PyCObject objects can
        wrap the same pointer), the object will be initialized as
        usual and returned.

        If a previous has been created based on the same pointer,
        then a reference to that object will be returned, and no
        object initialization is performed.
    """

    __instances = WeakValueDictionary()

    def __call__(cls, ptr, *args, **kwargs):
        id = _core.PyCObjectVoidPtrToPyLong(ptr)
        obj = ObjectCache.__instances.get(id)
        if obj is None:
            obj = super(ObjectCache, cls).__call__(ptr, *args, **kwargs)
            ObjectCache.__instances[id] = obj
        return obj

