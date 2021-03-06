#
# Copyright (c) 2008-10, Mahadevan R All rights reserved.
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

"""Intrinsic IDs.

Intended to be imported into the llvm.core namespace. Not for public use."""


INTR_ALPHA_UMULH                   = 1
INTR_ANNOTATION                    = 2
INTR_ARM_GET_FPSCR                 = 3
INTR_ARM_NEON_VABDS                = 4
INTR_ARM_NEON_VABDU                = 5
INTR_ARM_NEON_VABS                 = 6
INTR_ARM_NEON_VACGED               = 7
INTR_ARM_NEON_VACGEQ               = 8
INTR_ARM_NEON_VACGTD               = 9
INTR_ARM_NEON_VACGTQ               = 10
INTR_ARM_NEON_VADDHN               = 11
INTR_ARM_NEON_VCLS                 = 12
INTR_ARM_NEON_VCLZ                 = 13
INTR_ARM_NEON_VCNT                 = 14
INTR_ARM_NEON_VCVTFP2FXS           = 15
INTR_ARM_NEON_VCVTFP2FXU           = 16
INTR_ARM_NEON_VCVTFXS2FP           = 17
INTR_ARM_NEON_VCVTFXU2FP           = 18
INTR_ARM_NEON_VHADDS               = 19
INTR_ARM_NEON_VHADDU               = 20
INTR_ARM_NEON_VHSUBS               = 21
INTR_ARM_NEON_VHSUBU               = 22
INTR_ARM_NEON_VLD1                 = 23
INTR_ARM_NEON_VLD2                 = 24
INTR_ARM_NEON_VLD2LANE             = 25
INTR_ARM_NEON_VLD3                 = 26
INTR_ARM_NEON_VLD3LANE             = 27
INTR_ARM_NEON_VLD4                 = 28
INTR_ARM_NEON_VLD4LANE             = 29
INTR_ARM_NEON_VMAXS                = 30
INTR_ARM_NEON_VMAXU                = 31
INTR_ARM_NEON_VMINS                = 32
INTR_ARM_NEON_VMINU                = 33
INTR_ARM_NEON_VMULLP               = 34
INTR_ARM_NEON_VMULP                = 35
INTR_ARM_NEON_VPADALS              = 36
INTR_ARM_NEON_VPADALU              = 37
INTR_ARM_NEON_VPADD                = 38
INTR_ARM_NEON_VPADDLS              = 39
INTR_ARM_NEON_VPADDLU              = 40
INTR_ARM_NEON_VPMAXS               = 41
INTR_ARM_NEON_VPMAXU               = 42
INTR_ARM_NEON_VPMINS               = 43
INTR_ARM_NEON_VPMINU               = 44
INTR_ARM_NEON_VQABS                = 45
INTR_ARM_NEON_VQADDS               = 46
INTR_ARM_NEON_VQADDU               = 47
INTR_ARM_NEON_VQDMLAL              = 48
INTR_ARM_NEON_VQDMLSL              = 49
INTR_ARM_NEON_VQDMULH              = 50
INTR_ARM_NEON_VQDMULL              = 51
INTR_ARM_NEON_VQMOVNS              = 52
INTR_ARM_NEON_VQMOVNSU             = 53
INTR_ARM_NEON_VQMOVNU              = 54
INTR_ARM_NEON_VQNEG                = 55
INTR_ARM_NEON_VQRDMULH             = 56
INTR_ARM_NEON_VQRSHIFTNS           = 57
INTR_ARM_NEON_VQRSHIFTNSU          = 58
INTR_ARM_NEON_VQRSHIFTNU           = 59
INTR_ARM_NEON_VQRSHIFTS            = 60
INTR_ARM_NEON_VQRSHIFTU            = 61
INTR_ARM_NEON_VQSHIFTNS            = 62
INTR_ARM_NEON_VQSHIFTNSU           = 63
INTR_ARM_NEON_VQSHIFTNU            = 64
INTR_ARM_NEON_VQSHIFTS             = 65
INTR_ARM_NEON_VQSHIFTSU            = 66
INTR_ARM_NEON_VQSHIFTU             = 67
INTR_ARM_NEON_VQSUBS               = 68
INTR_ARM_NEON_VQSUBU               = 69
INTR_ARM_NEON_VRADDHN              = 70
INTR_ARM_NEON_VRECPE               = 71
INTR_ARM_NEON_VRECPS               = 72
INTR_ARM_NEON_VRHADDS              = 73
INTR_ARM_NEON_VRHADDU              = 74
INTR_ARM_NEON_VRSHIFTN             = 75
INTR_ARM_NEON_VRSHIFTS             = 76
INTR_ARM_NEON_VRSHIFTU             = 77
INTR_ARM_NEON_VRSQRTE              = 78
INTR_ARM_NEON_VRSQRTS              = 79
INTR_ARM_NEON_VRSUBHN              = 80
INTR_ARM_NEON_VSHIFTINS            = 81
INTR_ARM_NEON_VSHIFTLS             = 82
INTR_ARM_NEON_VSHIFTLU             = 83
INTR_ARM_NEON_VSHIFTN              = 84
INTR_ARM_NEON_VSHIFTS              = 85
INTR_ARM_NEON_VSHIFTU              = 86
INTR_ARM_NEON_VST1                 = 87
INTR_ARM_NEON_VST2                 = 88
INTR_ARM_NEON_VST2LANE             = 89
INTR_ARM_NEON_VST3                 = 90
INTR_ARM_NEON_VST3LANE             = 91
INTR_ARM_NEON_VST4                 = 92
INTR_ARM_NEON_VST4LANE             = 93
INTR_ARM_NEON_VSUBHN               = 94
INTR_ARM_NEON_VTBL1                = 95
INTR_ARM_NEON_VTBL2                = 96
INTR_ARM_NEON_VTBL3                = 97
INTR_ARM_NEON_VTBL4                = 98
INTR_ARM_NEON_VTBX1                = 99
INTR_ARM_NEON_VTBX2                = 100
INTR_ARM_NEON_VTBX3                = 101
INTR_ARM_NEON_VTBX4                = 102
INTR_ARM_QADD                      = 103
INTR_ARM_QSUB                      = 104
INTR_ARM_SET_FPSCR                 = 105
INTR_ARM_SSAT                      = 106
INTR_ARM_THREAD_POINTER            = 107
INTR_ARM_USAT                      = 108
INTR_ARM_VCVTR                     = 109
INTR_ARM_VCVTRU                    = 110
INTR_ATOMIC_CMP_SWAP               = 111
INTR_ATOMIC_LOAD_ADD               = 112
INTR_ATOMIC_LOAD_AND               = 113
INTR_ATOMIC_LOAD_MAX               = 114
INTR_ATOMIC_LOAD_MIN               = 115
INTR_ATOMIC_LOAD_NAND              = 116
INTR_ATOMIC_LOAD_OR                = 117
INTR_ATOMIC_LOAD_SUB               = 118
INTR_ATOMIC_LOAD_UMAX              = 119
INTR_ATOMIC_LOAD_UMIN              = 120
INTR_ATOMIC_LOAD_XOR               = 121
INTR_ATOMIC_SWAP                   = 122
INTR_BSWAP                         = 123
INTR_CONVERT_FROM_FP16             = 124
INTR_CONVERT_TO_FP16               = 125
INTR_CONVERTFF                     = 126
INTR_CONVERTFSI                    = 127
INTR_CONVERTFUI                    = 128
INTR_CONVERTSIF                    = 129
INTR_CONVERTSS                     = 130
INTR_CONVERTSU                     = 131
INTR_CONVERTUIF                    = 132
INTR_CONVERTUS                     = 133
INTR_CONVERTUU                     = 134
INTR_COS                           = 135
INTR_CTLZ                          = 136
INTR_CTPOP                         = 137
INTR_CTTZ                          = 138
INTR_DBG_DECLARE                   = 139
INTR_DBG_VALUE                     = 140
INTR_EH_DWARF_CFA                  = 141
INTR_EH_EXCEPTION                  = 142
INTR_EH_RETURN_I32                 = 143
INTR_EH_RETURN_I64                 = 144
INTR_EH_SELECTOR                   = 145
INTR_EH_SJLJ_CALLSITE              = 146
INTR_EH_SJLJ_LONGJMP               = 147
INTR_EH_SJLJ_LSDA                  = 148
INTR_EH_SJLJ_SETJMP                = 149
INTR_EH_TYPEID_FOR                 = 150
INTR_EH_UNWIND_INIT                = 151
INTR_EXP                           = 152
INTR_EXP2                          = 153
INTR_FLT_ROUNDS                    = 154
INTR_FRAMEADDRESS                  = 155
INTR_GCREAD                        = 156
INTR_GCROOT                        = 157
INTR_GCWRITE                       = 158
INTR_INIT_TRAMPOLINE               = 159
INTR_INVARIANT_END                 = 160
INTR_INVARIANT_START               = 161
INTR_LIFETIME_END                  = 162
INTR_LIFETIME_START                = 163
INTR_LOG                           = 164
INTR_LOG10                         = 165
INTR_LOG2                          = 166
INTR_LONGJMP                       = 167
INTR_MEMCPY                        = 168
INTR_MEMMOVE                       = 169
INTR_MEMORY_BARRIER                = 170
INTR_MEMSET                        = 171
INTR_OBJECTSIZE                    = 172
INTR_PCMARKER                      = 173
INTR_POW                           = 174
INTR_POWI                          = 175
INTR_PPC_ALTIVEC_DSS               = 176
INTR_PPC_ALTIVEC_DSSALL            = 177
INTR_PPC_ALTIVEC_DST               = 178
INTR_PPC_ALTIVEC_DSTST             = 179
INTR_PPC_ALTIVEC_DSTSTT            = 180
INTR_PPC_ALTIVEC_DSTT              = 181
INTR_PPC_ALTIVEC_LVEBX             = 182
INTR_PPC_ALTIVEC_LVEHX             = 183
INTR_PPC_ALTIVEC_LVEWX             = 184
INTR_PPC_ALTIVEC_LVSL              = 185
INTR_PPC_ALTIVEC_LVSR              = 186
INTR_PPC_ALTIVEC_LVX               = 187
INTR_PPC_ALTIVEC_LVXL              = 188
INTR_PPC_ALTIVEC_MFVSCR            = 189
INTR_PPC_ALTIVEC_MTVSCR            = 190
INTR_PPC_ALTIVEC_STVEBX            = 191
INTR_PPC_ALTIVEC_STVEHX            = 192
INTR_PPC_ALTIVEC_STVEWX            = 193
INTR_PPC_ALTIVEC_STVX              = 194
INTR_PPC_ALTIVEC_STVXL             = 195
INTR_PPC_ALTIVEC_VADDCUW           = 196
INTR_PPC_ALTIVEC_VADDSBS           = 197
INTR_PPC_ALTIVEC_VADDSHS           = 198
INTR_PPC_ALTIVEC_VADDSWS           = 199
INTR_PPC_ALTIVEC_VADDUBS           = 200
INTR_PPC_ALTIVEC_VADDUHS           = 201
INTR_PPC_ALTIVEC_VADDUWS           = 202
INTR_PPC_ALTIVEC_VAVGSB            = 203
INTR_PPC_ALTIVEC_VAVGSH            = 204
INTR_PPC_ALTIVEC_VAVGSW            = 205
INTR_PPC_ALTIVEC_VAVGUB            = 206
INTR_PPC_ALTIVEC_VAVGUH            = 207
INTR_PPC_ALTIVEC_VAVGUW            = 208
INTR_PPC_ALTIVEC_VCFSX             = 209
INTR_PPC_ALTIVEC_VCFUX             = 210
INTR_PPC_ALTIVEC_VCMPBFP           = 211
INTR_PPC_ALTIVEC_VCMPBFP_P         = 212
INTR_PPC_ALTIVEC_VCMPEQFP          = 213
INTR_PPC_ALTIVEC_VCMPEQFP_P        = 214
INTR_PPC_ALTIVEC_VCMPEQUB          = 215
INTR_PPC_ALTIVEC_VCMPEQUB_P        = 216
INTR_PPC_ALTIVEC_VCMPEQUH          = 217
INTR_PPC_ALTIVEC_VCMPEQUH_P        = 218
INTR_PPC_ALTIVEC_VCMPEQUW          = 219
INTR_PPC_ALTIVEC_VCMPEQUW_P        = 220
INTR_PPC_ALTIVEC_VCMPGEFP          = 221
INTR_PPC_ALTIVEC_VCMPGEFP_P        = 222
INTR_PPC_ALTIVEC_VCMPGTFP          = 223
INTR_PPC_ALTIVEC_VCMPGTFP_P        = 224
INTR_PPC_ALTIVEC_VCMPGTSB          = 225
INTR_PPC_ALTIVEC_VCMPGTSB_P        = 226
INTR_PPC_ALTIVEC_VCMPGTSH          = 227
INTR_PPC_ALTIVEC_VCMPGTSH_P        = 228
INTR_PPC_ALTIVEC_VCMPGTSW          = 229
INTR_PPC_ALTIVEC_VCMPGTSW_P        = 230
INTR_PPC_ALTIVEC_VCMPGTUB          = 231
INTR_PPC_ALTIVEC_VCMPGTUB_P        = 232
INTR_PPC_ALTIVEC_VCMPGTUH          = 233
INTR_PPC_ALTIVEC_VCMPGTUH_P        = 234
INTR_PPC_ALTIVEC_VCMPGTUW          = 235
INTR_PPC_ALTIVEC_VCMPGTUW_P        = 236
INTR_PPC_ALTIVEC_VCTSXS            = 237
INTR_PPC_ALTIVEC_VCTUXS            = 238
INTR_PPC_ALTIVEC_VEXPTEFP          = 239
INTR_PPC_ALTIVEC_VLOGEFP           = 240
INTR_PPC_ALTIVEC_VMADDFP           = 241
INTR_PPC_ALTIVEC_VMAXFP            = 242
INTR_PPC_ALTIVEC_VMAXSB            = 243
INTR_PPC_ALTIVEC_VMAXSH            = 244
INTR_PPC_ALTIVEC_VMAXSW            = 245
INTR_PPC_ALTIVEC_VMAXUB            = 246
INTR_PPC_ALTIVEC_VMAXUH            = 247
INTR_PPC_ALTIVEC_VMAXUW            = 248
INTR_PPC_ALTIVEC_VMHADDSHS         = 249
INTR_PPC_ALTIVEC_VMHRADDSHS        = 250
INTR_PPC_ALTIVEC_VMINFP            = 251
INTR_PPC_ALTIVEC_VMINSB            = 252
INTR_PPC_ALTIVEC_VMINSH            = 253
INTR_PPC_ALTIVEC_VMINSW            = 254
INTR_PPC_ALTIVEC_VMINUB            = 255
INTR_PPC_ALTIVEC_VMINUH            = 256
INTR_PPC_ALTIVEC_VMINUW            = 257
INTR_PPC_ALTIVEC_VMLADDUHM         = 258
INTR_PPC_ALTIVEC_VMSUMMBM          = 259
INTR_PPC_ALTIVEC_VMSUMSHM          = 260
INTR_PPC_ALTIVEC_VMSUMSHS          = 261
INTR_PPC_ALTIVEC_VMSUMUBM          = 262
INTR_PPC_ALTIVEC_VMSUMUHM          = 263
INTR_PPC_ALTIVEC_VMSUMUHS          = 264
INTR_PPC_ALTIVEC_VMULESB           = 265
INTR_PPC_ALTIVEC_VMULESH           = 266
INTR_PPC_ALTIVEC_VMULEUB           = 267
INTR_PPC_ALTIVEC_VMULEUH           = 268
INTR_PPC_ALTIVEC_VMULOSB           = 269
INTR_PPC_ALTIVEC_VMULOSH           = 270
INTR_PPC_ALTIVEC_VMULOUB           = 271
INTR_PPC_ALTIVEC_VMULOUH           = 272
INTR_PPC_ALTIVEC_VNMSUBFP          = 273
INTR_PPC_ALTIVEC_VPERM             = 274
INTR_PPC_ALTIVEC_VPKPX             = 275
INTR_PPC_ALTIVEC_VPKSHSS           = 276
INTR_PPC_ALTIVEC_VPKSHUS           = 277
INTR_PPC_ALTIVEC_VPKSWSS           = 278
INTR_PPC_ALTIVEC_VPKSWUS           = 279
INTR_PPC_ALTIVEC_VPKUHUS           = 280
INTR_PPC_ALTIVEC_VPKUWUS           = 281
INTR_PPC_ALTIVEC_VREFP             = 282
INTR_PPC_ALTIVEC_VRFIM             = 283
INTR_PPC_ALTIVEC_VRFIN             = 284
INTR_PPC_ALTIVEC_VRFIP             = 285
INTR_PPC_ALTIVEC_VRFIZ             = 286
INTR_PPC_ALTIVEC_VRLB              = 287
INTR_PPC_ALTIVEC_VRLH              = 288
INTR_PPC_ALTIVEC_VRLW              = 289
INTR_PPC_ALTIVEC_VRSQRTEFP         = 290
INTR_PPC_ALTIVEC_VSEL              = 291
INTR_PPC_ALTIVEC_VSL               = 292
INTR_PPC_ALTIVEC_VSLB              = 293
INTR_PPC_ALTIVEC_VSLH              = 294
INTR_PPC_ALTIVEC_VSLO              = 295
INTR_PPC_ALTIVEC_VSLW              = 296
INTR_PPC_ALTIVEC_VSR               = 297
INTR_PPC_ALTIVEC_VSRAB             = 298
INTR_PPC_ALTIVEC_VSRAH             = 299
INTR_PPC_ALTIVEC_VSRAW             = 300
INTR_PPC_ALTIVEC_VSRB              = 301
INTR_PPC_ALTIVEC_VSRH              = 302
INTR_PPC_ALTIVEC_VSRO              = 303
INTR_PPC_ALTIVEC_VSRW              = 304
INTR_PPC_ALTIVEC_VSUBCUW           = 305
INTR_PPC_ALTIVEC_VSUBSBS           = 306
INTR_PPC_ALTIVEC_VSUBSHS           = 307
INTR_PPC_ALTIVEC_VSUBSWS           = 308
INTR_PPC_ALTIVEC_VSUBUBS           = 309
INTR_PPC_ALTIVEC_VSUBUHS           = 310
INTR_PPC_ALTIVEC_VSUBUWS           = 311
INTR_PPC_ALTIVEC_VSUM2SWS          = 312
INTR_PPC_ALTIVEC_VSUM4SBS          = 313
INTR_PPC_ALTIVEC_VSUM4SHS          = 314
INTR_PPC_ALTIVEC_VSUM4UBS          = 315
INTR_PPC_ALTIVEC_VSUMSWS           = 316
INTR_PPC_ALTIVEC_VUPKHPX           = 317
INTR_PPC_ALTIVEC_VUPKHSB           = 318
INTR_PPC_ALTIVEC_VUPKHSH           = 319
INTR_PPC_ALTIVEC_VUPKLPX           = 320
INTR_PPC_ALTIVEC_VUPKLSB           = 321
INTR_PPC_ALTIVEC_VUPKLSH           = 322
INTR_PPC_DCBA                      = 323
INTR_PPC_DCBF                      = 324
INTR_PPC_DCBI                      = 325
INTR_PPC_DCBST                     = 326
INTR_PPC_DCBT                      = 327
INTR_PPC_DCBTST                    = 328
INTR_PPC_DCBZ                      = 329
INTR_PPC_DCBZL                     = 330
INTR_PPC_SYNC                      = 331
INTR_PREFETCH                      = 332
INTR_PTR_ANNOTATION                = 333
INTR_READCYCLECOUNTER              = 334
INTR_RETURNADDRESS                 = 335
INTR_SADD_WITH_OVERFLOW            = 336
INTR_SETJMP                        = 337
INTR_SIGLONGJMP                    = 338
INTR_SIGSETJMP                     = 339
INTR_SIN                           = 340
INTR_SMUL_WITH_OVERFLOW            = 341
INTR_SPU_SI_A                      = 342
INTR_SPU_SI_ADDX                   = 343
INTR_SPU_SI_AH                     = 344
INTR_SPU_SI_AHI                    = 345
INTR_SPU_SI_AI                     = 346
INTR_SPU_SI_AND                    = 347
INTR_SPU_SI_ANDBI                  = 348
INTR_SPU_SI_ANDC                   = 349
INTR_SPU_SI_ANDHI                  = 350
INTR_SPU_SI_ANDI                   = 351
INTR_SPU_SI_BG                     = 352
INTR_SPU_SI_BGX                    = 353
INTR_SPU_SI_CEQ                    = 354
INTR_SPU_SI_CEQB                   = 355
INTR_SPU_SI_CEQBI                  = 356
INTR_SPU_SI_CEQH                   = 357
INTR_SPU_SI_CEQHI                  = 358
INTR_SPU_SI_CEQI                   = 359
INTR_SPU_SI_CG                     = 360
INTR_SPU_SI_CGT                    = 361
INTR_SPU_SI_CGTB                   = 362
INTR_SPU_SI_CGTBI                  = 363
INTR_SPU_SI_CGTH                   = 364
INTR_SPU_SI_CGTHI                  = 365
INTR_SPU_SI_CGTI                   = 366
INTR_SPU_SI_CGX                    = 367
INTR_SPU_SI_CLGT                   = 368
INTR_SPU_SI_CLGTB                  = 369
INTR_SPU_SI_CLGTBI                 = 370
INTR_SPU_SI_CLGTH                  = 371
INTR_SPU_SI_CLGTHI                 = 372
INTR_SPU_SI_CLGTI                  = 373
INTR_SPU_SI_DFA                    = 374
INTR_SPU_SI_DFM                    = 375
INTR_SPU_SI_DFMA                   = 376
INTR_SPU_SI_DFMS                   = 377
INTR_SPU_SI_DFNMA                  = 378
INTR_SPU_SI_DFNMS                  = 379
INTR_SPU_SI_DFS                    = 380
INTR_SPU_SI_FA                     = 381
INTR_SPU_SI_FCEQ                   = 382
INTR_SPU_SI_FCGT                   = 383
INTR_SPU_SI_FCMEQ                  = 384
INTR_SPU_SI_FCMGT                  = 385
INTR_SPU_SI_FM                     = 386
INTR_SPU_SI_FMA                    = 387
INTR_SPU_SI_FMS                    = 388
INTR_SPU_SI_FNMS                   = 389
INTR_SPU_SI_FS                     = 390
INTR_SPU_SI_FSMBI                  = 391
INTR_SPU_SI_MPY                    = 392
INTR_SPU_SI_MPYA                   = 393
INTR_SPU_SI_MPYH                   = 394
INTR_SPU_SI_MPYHH                  = 395
INTR_SPU_SI_MPYHHA                 = 396
INTR_SPU_SI_MPYHHAU                = 397
INTR_SPU_SI_MPYHHU                 = 398
INTR_SPU_SI_MPYI                   = 399
INTR_SPU_SI_MPYS                   = 400
INTR_SPU_SI_MPYU                   = 401
INTR_SPU_SI_MPYUI                  = 402
INTR_SPU_SI_NAND                   = 403
INTR_SPU_SI_NOR                    = 404
INTR_SPU_SI_OR                     = 405
INTR_SPU_SI_ORBI                   = 406
INTR_SPU_SI_ORC                    = 407
INTR_SPU_SI_ORHI                   = 408
INTR_SPU_SI_ORI                    = 409
INTR_SPU_SI_SF                     = 410
INTR_SPU_SI_SFH                    = 411
INTR_SPU_SI_SFHI                   = 412
INTR_SPU_SI_SFI                    = 413
INTR_SPU_SI_SFX                    = 414
INTR_SPU_SI_SHLI                   = 415
INTR_SPU_SI_SHLQBI                 = 416
INTR_SPU_SI_SHLQBII                = 417
INTR_SPU_SI_SHLQBY                 = 418
INTR_SPU_SI_SHLQBYI                = 419
INTR_SPU_SI_XOR                    = 420
INTR_SPU_SI_XORBI                  = 421
INTR_SPU_SI_XORHI                  = 422
INTR_SPU_SI_XORI                   = 423
INTR_SQRT                          = 424
INTR_SSUB_WITH_OVERFLOW            = 425
INTR_STACKPROTECTOR                = 426
INTR_STACKRESTORE                  = 427
INTR_STACKSAVE                     = 428
INTR_TRAP                          = 429
INTR_UADD_WITH_OVERFLOW            = 430
INTR_UMUL_WITH_OVERFLOW            = 431
INTR_USUB_WITH_OVERFLOW            = 432
INTR_VACOPY                        = 433
INTR_VAEND                         = 434
INTR_VAR_ANNOTATION                = 435
INTR_VASTART                       = 436
INTR_X86_AESNI_AESDEC              = 437
INTR_X86_AESNI_AESDECLAST          = 438
INTR_X86_AESNI_AESENC              = 439
INTR_X86_AESNI_AESENCLAST          = 440
INTR_X86_AESNI_AESIMC              = 441
INTR_X86_AESNI_AESKEYGENASSIST     = 442
INTR_X86_AVX_ADDSUB_PD_256         = 443
INTR_X86_AVX_ADDSUB_PS_256         = 444
INTR_X86_AVX_BLEND_PD_256          = 445
INTR_X86_AVX_BLEND_PS_256          = 446
INTR_X86_AVX_BLENDV_PD_256         = 447
INTR_X86_AVX_BLENDV_PS_256         = 448
INTR_X86_AVX_CMP_PD_256            = 449
INTR_X86_AVX_CMP_PS_256            = 450
INTR_X86_AVX_CVT_PD2_PS_256        = 451
INTR_X86_AVX_CVT_PD2DQ_256         = 452
INTR_X86_AVX_CVT_PS2_PD_256        = 453
INTR_X86_AVX_CVT_PS2DQ_256         = 454
INTR_X86_AVX_CVTDQ2_PD_256         = 455
INTR_X86_AVX_CVTDQ2_PS_256         = 456
INTR_X86_AVX_CVTT_PD2DQ_256        = 457
INTR_X86_AVX_CVTT_PS2DQ_256        = 458
INTR_X86_AVX_DP_PS_256             = 459
INTR_X86_AVX_HADD_PD_256           = 460
INTR_X86_AVX_HADD_PS_256           = 461
INTR_X86_AVX_HSUB_PD_256           = 462
INTR_X86_AVX_HSUB_PS_256           = 463
INTR_X86_AVX_LDU_DQ_256            = 464
INTR_X86_AVX_LOADU_DQ_256          = 465
INTR_X86_AVX_LOADU_PD_256          = 466
INTR_X86_AVX_LOADU_PS_256          = 467
INTR_X86_AVX_MASKLOAD_PD           = 468
INTR_X86_AVX_MASKLOAD_PD_256       = 469
INTR_X86_AVX_MASKLOAD_PS           = 470
INTR_X86_AVX_MASKLOAD_PS_256       = 471
INTR_X86_AVX_MASKSTORE_PD          = 472
INTR_X86_AVX_MASKSTORE_PD_256      = 473
INTR_X86_AVX_MASKSTORE_PS          = 474
INTR_X86_AVX_MASKSTORE_PS_256      = 475
INTR_X86_AVX_MAX_PD_256            = 476
INTR_X86_AVX_MAX_PS_256            = 477
INTR_X86_AVX_MIN_PD_256            = 478
INTR_X86_AVX_MIN_PS_256            = 479
INTR_X86_AVX_MOVMSK_PD_256         = 480
INTR_X86_AVX_MOVMSK_PS_256         = 481
INTR_X86_AVX_MOVNT_DQ_256          = 482
INTR_X86_AVX_MOVNT_PD_256          = 483
INTR_X86_AVX_MOVNT_PS_256          = 484
INTR_X86_AVX_PTESTC_256            = 485
INTR_X86_AVX_PTESTNZC_256          = 486
INTR_X86_AVX_PTESTZ_256            = 487
INTR_X86_AVX_RCP_PS_256            = 488
INTR_X86_AVX_ROUND_PD_256          = 489
INTR_X86_AVX_ROUND_PS_256          = 490
INTR_X86_AVX_RSQRT_PS_256          = 491
INTR_X86_AVX_SQRT_PD_256           = 492
INTR_X86_AVX_SQRT_PS_256           = 493
INTR_X86_AVX_STOREU_DQ_256         = 494
INTR_X86_AVX_STOREU_PD_256         = 495
INTR_X86_AVX_STOREU_PS_256         = 496
INTR_X86_AVX_VBROADCAST_SD_256     = 497
INTR_X86_AVX_VBROADCASTF128_PD_256 = 498
INTR_X86_AVX_VBROADCASTF128_PS_256 = 499
INTR_X86_AVX_VBROADCASTSS          = 500
INTR_X86_AVX_VBROADCASTSS_256      = 501
INTR_X86_AVX_VEXTRACTF128_PD_256   = 502
INTR_X86_AVX_VEXTRACTF128_PS_256   = 503
INTR_X86_AVX_VEXTRACTF128_SI_256   = 504
INTR_X86_AVX_VINSERTF128_PD_256    = 505
INTR_X86_AVX_VINSERTF128_PS_256    = 506
INTR_X86_AVX_VINSERTF128_SI_256    = 507
INTR_X86_AVX_VPERM2F128_PD_256     = 508
INTR_X86_AVX_VPERM2F128_PS_256     = 509
INTR_X86_AVX_VPERM2F128_SI_256     = 510
INTR_X86_AVX_VPERMIL_PD            = 511
INTR_X86_AVX_VPERMIL_PD_256        = 512
INTR_X86_AVX_VPERMIL_PS            = 513
INTR_X86_AVX_VPERMIL_PS_256        = 514
INTR_X86_AVX_VPERMILVAR_PD         = 515
INTR_X86_AVX_VPERMILVAR_PD_256     = 516
INTR_X86_AVX_VPERMILVAR_PS         = 517
INTR_X86_AVX_VPERMILVAR_PS_256     = 518
INTR_X86_AVX_VTESTC_PD             = 519
INTR_X86_AVX_VTESTC_PD_256         = 520
INTR_X86_AVX_VTESTC_PS             = 521
INTR_X86_AVX_VTESTC_PS_256         = 522
INTR_X86_AVX_VTESTNZC_PD           = 523
INTR_X86_AVX_VTESTNZC_PD_256       = 524
INTR_X86_AVX_VTESTNZC_PS           = 525
INTR_X86_AVX_VTESTNZC_PS_256       = 526
INTR_X86_AVX_VTESTZ_PD             = 527
INTR_X86_AVX_VTESTZ_PD_256         = 528
INTR_X86_AVX_VTESTZ_PS             = 529
INTR_X86_AVX_VTESTZ_PS_256         = 530
INTR_X86_AVX_VZEROALL              = 531
INTR_X86_AVX_VZEROUPPER            = 532
INTR_X86_INT                       = 533
INTR_X86_MMX_CVTSI32_SI64          = 534
INTR_X86_MMX_CVTSI64_SI32          = 535
INTR_X86_MMX_EMMS                  = 536
INTR_X86_MMX_FEMMS                 = 537
INTR_X86_MMX_MASKMOVQ              = 538
INTR_X86_MMX_MOVNT_DQ              = 539
INTR_X86_MMX_PACKSSDW              = 540
INTR_X86_MMX_PACKSSWB              = 541
INTR_X86_MMX_PACKUSWB              = 542
INTR_X86_MMX_PADD_B                = 543
INTR_X86_MMX_PADD_D                = 544
INTR_X86_MMX_PADD_Q                = 545
INTR_X86_MMX_PADD_W                = 546
INTR_X86_MMX_PADDS_B               = 547
INTR_X86_MMX_PADDS_W               = 548
INTR_X86_MMX_PADDUS_B              = 549
INTR_X86_MMX_PADDUS_W              = 550
INTR_X86_MMX_PAND                  = 551
INTR_X86_MMX_PANDN                 = 552
INTR_X86_MMX_PAVG_B                = 553
INTR_X86_MMX_PAVG_W                = 554
INTR_X86_MMX_PCMPEQ_B              = 555
INTR_X86_MMX_PCMPEQ_D              = 556
INTR_X86_MMX_PCMPEQ_W              = 557
INTR_X86_MMX_PCMPGT_B              = 558
INTR_X86_MMX_PCMPGT_D              = 559
INTR_X86_MMX_PCMPGT_W              = 560
INTR_X86_MMX_PEXTR_W               = 561
INTR_X86_MMX_PINSR_W               = 562
INTR_X86_MMX_PMADD_WD              = 563
INTR_X86_MMX_PMAXS_W               = 564
INTR_X86_MMX_PMAXU_B               = 565
INTR_X86_MMX_PMINS_W               = 566
INTR_X86_MMX_PMINU_B               = 567
INTR_X86_MMX_PMOVMSKB              = 568
INTR_X86_MMX_PMULH_W               = 569
INTR_X86_MMX_PMULHU_W              = 570
INTR_X86_MMX_PMULL_W               = 571
INTR_X86_MMX_PMULU_DQ              = 572
INTR_X86_MMX_POR                   = 573
INTR_X86_MMX_PSAD_BW               = 574
INTR_X86_MMX_PSLL_D                = 575
INTR_X86_MMX_PSLL_Q                = 576
INTR_X86_MMX_PSLL_W                = 577
INTR_X86_MMX_PSLLI_D               = 578
INTR_X86_MMX_PSLLI_Q               = 579
INTR_X86_MMX_PSLLI_W               = 580
INTR_X86_MMX_PSRA_D                = 581
INTR_X86_MMX_PSRA_W                = 582
INTR_X86_MMX_PSRAI_D               = 583
INTR_X86_MMX_PSRAI_W               = 584
INTR_X86_MMX_PSRL_D                = 585
INTR_X86_MMX_PSRL_Q                = 586
INTR_X86_MMX_PSRL_W                = 587
INTR_X86_MMX_PSRLI_D               = 588
INTR_X86_MMX_PSRLI_Q               = 589
INTR_X86_MMX_PSRLI_W               = 590
INTR_X86_MMX_PSUB_B                = 591
INTR_X86_MMX_PSUB_D                = 592
INTR_X86_MMX_PSUB_Q                = 593
INTR_X86_MMX_PSUB_W                = 594
INTR_X86_MMX_PSUBS_B               = 595
INTR_X86_MMX_PSUBS_W               = 596
INTR_X86_MMX_PSUBUS_B              = 597
INTR_X86_MMX_PSUBUS_W              = 598
INTR_X86_MMX_PUNPCKHBW             = 599
INTR_X86_MMX_PUNPCKHDQ             = 600
INTR_X86_MMX_PUNPCKHWD             = 601
INTR_X86_MMX_PUNPCKLBW             = 602
INTR_X86_MMX_PUNPCKLDQ             = 603
INTR_X86_MMX_PUNPCKLWD             = 604
INTR_X86_MMX_PXOR                  = 605
INTR_X86_MMX_VEC_EXT_D             = 606
INTR_X86_MMX_VEC_INIT_B            = 607
INTR_X86_MMX_VEC_INIT_D            = 608
INTR_X86_MMX_VEC_INIT_W            = 609
INTR_X86_SSE2_ADD_SD               = 610
INTR_X86_SSE2_CLFLUSH              = 611
INTR_X86_SSE2_CMP_PD               = 612
INTR_X86_SSE2_CMP_SD               = 613
INTR_X86_SSE2_COMIEQ_SD            = 614
INTR_X86_SSE2_COMIGE_SD            = 615
INTR_X86_SSE2_COMIGT_SD            = 616
INTR_X86_SSE2_COMILE_SD            = 617
INTR_X86_SSE2_COMILT_SD            = 618
INTR_X86_SSE2_COMINEQ_SD           = 619
INTR_X86_SSE2_CVTDQ2PD             = 620
INTR_X86_SSE2_CVTDQ2PS             = 621
INTR_X86_SSE2_CVTPD2DQ             = 622
INTR_X86_SSE2_CVTPD2PS             = 623
INTR_X86_SSE2_CVTPS2DQ             = 624
INTR_X86_SSE2_CVTPS2PD             = 625
INTR_X86_SSE2_CVTSD2SI             = 626
INTR_X86_SSE2_CVTSD2SI64           = 627
INTR_X86_SSE2_CVTSD2SS             = 628
INTR_X86_SSE2_CVTSI2SD             = 629
INTR_X86_SSE2_CVTSI642SD           = 630
INTR_X86_SSE2_CVTSS2SD             = 631
INTR_X86_SSE2_CVTTPD2DQ            = 632
INTR_X86_SSE2_CVTTPS2DQ            = 633
INTR_X86_SSE2_CVTTSD2SI            = 634
INTR_X86_SSE2_CVTTSD2SI64          = 635
INTR_X86_SSE2_DIV_SD               = 636
INTR_X86_SSE2_LFENCE               = 637
INTR_X86_SSE2_LOADU_DQ             = 638
INTR_X86_SSE2_LOADU_PD             = 639
INTR_X86_SSE2_MASKMOV_DQU          = 640
INTR_X86_SSE2_MAX_PD               = 641
INTR_X86_SSE2_MAX_SD               = 642
INTR_X86_SSE2_MFENCE               = 643
INTR_X86_SSE2_MIN_PD               = 644
INTR_X86_SSE2_MIN_SD               = 645
INTR_X86_SSE2_MOVMSK_PD            = 646
INTR_X86_SSE2_MOVNT_DQ             = 647
INTR_X86_SSE2_MOVNT_I              = 648
INTR_X86_SSE2_MOVNT_PD             = 649
INTR_X86_SSE2_MUL_SD               = 650
INTR_X86_SSE2_PACKSSDW_128         = 651
INTR_X86_SSE2_PACKSSWB_128         = 652
INTR_X86_SSE2_PACKUSWB_128         = 653
INTR_X86_SSE2_PADDS_B              = 654
INTR_X86_SSE2_PADDS_W              = 655
INTR_X86_SSE2_PADDUS_B             = 656
INTR_X86_SSE2_PADDUS_W             = 657
INTR_X86_SSE2_PAVG_B               = 658
INTR_X86_SSE2_PAVG_W               = 659
INTR_X86_SSE2_PCMPEQ_B             = 660
INTR_X86_SSE2_PCMPEQ_D             = 661
INTR_X86_SSE2_PCMPEQ_W             = 662
INTR_X86_SSE2_PCMPGT_B             = 663
INTR_X86_SSE2_PCMPGT_D             = 664
INTR_X86_SSE2_PCMPGT_W             = 665
INTR_X86_SSE2_PMADD_WD             = 666
INTR_X86_SSE2_PMAXS_W              = 667
INTR_X86_SSE2_PMAXU_B              = 668
INTR_X86_SSE2_PMINS_W              = 669
INTR_X86_SSE2_PMINU_B              = 670
INTR_X86_SSE2_PMOVMSKB_128         = 671
INTR_X86_SSE2_PMULH_W              = 672
INTR_X86_SSE2_PMULHU_W             = 673
INTR_X86_SSE2_PMULU_DQ             = 674
INTR_X86_SSE2_PSAD_BW              = 675
INTR_X86_SSE2_PSLL_D               = 676
INTR_X86_SSE2_PSLL_DQ              = 677
INTR_X86_SSE2_PSLL_DQ_BS           = 678
INTR_X86_SSE2_PSLL_Q               = 679
INTR_X86_SSE2_PSLL_W               = 680
INTR_X86_SSE2_PSLLI_D              = 681
INTR_X86_SSE2_PSLLI_Q              = 682
INTR_X86_SSE2_PSLLI_W              = 683
INTR_X86_SSE2_PSRA_D               = 684
INTR_X86_SSE2_PSRA_W               = 685
INTR_X86_SSE2_PSRAI_D              = 686
INTR_X86_SSE2_PSRAI_W              = 687
INTR_X86_SSE2_PSRL_D               = 688
INTR_X86_SSE2_PSRL_DQ              = 689
INTR_X86_SSE2_PSRL_DQ_BS           = 690
INTR_X86_SSE2_PSRL_Q               = 691
INTR_X86_SSE2_PSRL_W               = 692
INTR_X86_SSE2_PSRLI_D              = 693
INTR_X86_SSE2_PSRLI_Q              = 694
INTR_X86_SSE2_PSRLI_W              = 695
INTR_X86_SSE2_PSUBS_B              = 696
INTR_X86_SSE2_PSUBS_W              = 697
INTR_X86_SSE2_PSUBUS_B             = 698
INTR_X86_SSE2_PSUBUS_W             = 699
INTR_X86_SSE2_SQRT_PD              = 700
INTR_X86_SSE2_SQRT_SD              = 701
INTR_X86_SSE2_STOREL_DQ            = 702
INTR_X86_SSE2_STOREU_DQ            = 703
INTR_X86_SSE2_STOREU_PD            = 704
INTR_X86_SSE2_SUB_SD               = 705
INTR_X86_SSE2_UCOMIEQ_SD           = 706
INTR_X86_SSE2_UCOMIGE_SD           = 707
INTR_X86_SSE2_UCOMIGT_SD           = 708
INTR_X86_SSE2_UCOMILE_SD           = 709
INTR_X86_SSE2_UCOMILT_SD           = 710
INTR_X86_SSE2_UCOMINEQ_SD          = 711
INTR_X86_SSE3_ADDSUB_PD            = 712
INTR_X86_SSE3_ADDSUB_PS            = 713
INTR_X86_SSE3_HADD_PD              = 714
INTR_X86_SSE3_HADD_PS              = 715
INTR_X86_SSE3_HSUB_PD              = 716
INTR_X86_SSE3_HSUB_PS              = 717
INTR_X86_SSE3_LDU_DQ               = 718
INTR_X86_SSE3_MONITOR              = 719
INTR_X86_SSE3_MWAIT                = 720
INTR_X86_SSE41_BLENDPD             = 721
INTR_X86_SSE41_BLENDPS             = 722
INTR_X86_SSE41_BLENDVPD            = 723
INTR_X86_SSE41_BLENDVPS            = 724
INTR_X86_SSE41_DPPD                = 725
INTR_X86_SSE41_DPPS                = 726
INTR_X86_SSE41_EXTRACTPS           = 727
INTR_X86_SSE41_INSERTPS            = 728
INTR_X86_SSE41_MOVNTDQA            = 729
INTR_X86_SSE41_MPSADBW             = 730
INTR_X86_SSE41_PACKUSDW            = 731
INTR_X86_SSE41_PBLENDVB            = 732
INTR_X86_SSE41_PBLENDW             = 733
INTR_X86_SSE41_PCMPEQQ             = 734
INTR_X86_SSE41_PEXTRB              = 735
INTR_X86_SSE41_PEXTRD              = 736
INTR_X86_SSE41_PEXTRQ              = 737
INTR_X86_SSE41_PHMINPOSUW          = 738
INTR_X86_SSE41_PMAXSB              = 739
INTR_X86_SSE41_PMAXSD              = 740
INTR_X86_SSE41_PMAXUD              = 741
INTR_X86_SSE41_PMAXUW              = 742
INTR_X86_SSE41_PMINSB              = 743
INTR_X86_SSE41_PMINSD              = 744
INTR_X86_SSE41_PMINUD              = 745
INTR_X86_SSE41_PMINUW              = 746
INTR_X86_SSE41_PMOVSXBD            = 747
INTR_X86_SSE41_PMOVSXBQ            = 748
INTR_X86_SSE41_PMOVSXBW            = 749
INTR_X86_SSE41_PMOVSXDQ            = 750
INTR_X86_SSE41_PMOVSXWD            = 751
INTR_X86_SSE41_PMOVSXWQ            = 752
INTR_X86_SSE41_PMOVZXBD            = 753
INTR_X86_SSE41_PMOVZXBQ            = 754
INTR_X86_SSE41_PMOVZXBW            = 755
INTR_X86_SSE41_PMOVZXDQ            = 756
INTR_X86_SSE41_PMOVZXWD            = 757
INTR_X86_SSE41_PMOVZXWQ            = 758
INTR_X86_SSE41_PMULDQ              = 759
INTR_X86_SSE41_PTESTC              = 760
INTR_X86_SSE41_PTESTNZC            = 761
INTR_X86_SSE41_PTESTZ              = 762
INTR_X86_SSE41_ROUND_PD            = 763
INTR_X86_SSE41_ROUND_PS            = 764
INTR_X86_SSE41_ROUND_SD            = 765
INTR_X86_SSE41_ROUND_SS            = 766
INTR_X86_SSE42_CRC32_16            = 767
INTR_X86_SSE42_CRC32_32            = 768
INTR_X86_SSE42_CRC32_8             = 769
INTR_X86_SSE42_CRC64_64            = 770
INTR_X86_SSE42_CRC64_8             = 771
INTR_X86_SSE42_PCMPESTRI128        = 772
INTR_X86_SSE42_PCMPESTRIA128       = 773
INTR_X86_SSE42_PCMPESTRIC128       = 774
INTR_X86_SSE42_PCMPESTRIO128       = 775
INTR_X86_SSE42_PCMPESTRIS128       = 776
INTR_X86_SSE42_PCMPESTRIZ128       = 777
INTR_X86_SSE42_PCMPESTRM128        = 778
INTR_X86_SSE42_PCMPGTQ             = 779
INTR_X86_SSE42_PCMPISTRI128        = 780
INTR_X86_SSE42_PCMPISTRIA128       = 781
INTR_X86_SSE42_PCMPISTRIC128       = 782
INTR_X86_SSE42_PCMPISTRIO128       = 783
INTR_X86_SSE42_PCMPISTRIS128       = 784
INTR_X86_SSE42_PCMPISTRIZ128       = 785
INTR_X86_SSE42_PCMPISTRM128        = 786
INTR_X86_SSE_ADD_SS                = 787
INTR_X86_SSE_CMP_PS                = 788
INTR_X86_SSE_CMP_SS                = 789
INTR_X86_SSE_COMIEQ_SS             = 790
INTR_X86_SSE_COMIGE_SS             = 791
INTR_X86_SSE_COMIGT_SS             = 792
INTR_X86_SSE_COMILE_SS             = 793
INTR_X86_SSE_COMILT_SS             = 794
INTR_X86_SSE_COMINEQ_SS            = 795
INTR_X86_SSE_CVTPD2PI              = 796
INTR_X86_SSE_CVTPI2PD              = 797
INTR_X86_SSE_CVTPI2PS              = 798
INTR_X86_SSE_CVTPS2PI              = 799
INTR_X86_SSE_CVTSI2SS              = 800
INTR_X86_SSE_CVTSI642SS            = 801
INTR_X86_SSE_CVTSS2SI              = 802
INTR_X86_SSE_CVTSS2SI64            = 803
INTR_X86_SSE_CVTTPD2PI             = 804
INTR_X86_SSE_CVTTPS2PI             = 805
INTR_X86_SSE_CVTTSS2SI             = 806
INTR_X86_SSE_CVTTSS2SI64           = 807
INTR_X86_SSE_DIV_SS                = 808
INTR_X86_SSE_LDMXCSR               = 809
INTR_X86_SSE_LOADU_PS              = 810
INTR_X86_SSE_MAX_PS                = 811
INTR_X86_SSE_MAX_SS                = 812
INTR_X86_SSE_MIN_PS                = 813
INTR_X86_SSE_MIN_SS                = 814
INTR_X86_SSE_MOVMSK_PS             = 815
INTR_X86_SSE_MOVNT_PS              = 816
INTR_X86_SSE_MUL_SS                = 817
INTR_X86_SSE_RCP_PS                = 818
INTR_X86_SSE_RCP_SS                = 819
INTR_X86_SSE_RSQRT_PS              = 820
INTR_X86_SSE_RSQRT_SS              = 821
INTR_X86_SSE_SFENCE                = 822
INTR_X86_SSE_SQRT_PS               = 823
INTR_X86_SSE_SQRT_SS               = 824
INTR_X86_SSE_STMXCSR               = 825
INTR_X86_SSE_STOREU_PS             = 826
INTR_X86_SSE_SUB_SS                = 827
INTR_X86_SSE_UCOMIEQ_SS            = 828
INTR_X86_SSE_UCOMIGE_SS            = 829
INTR_X86_SSE_UCOMIGT_SS            = 830
INTR_X86_SSE_UCOMILE_SS            = 831
INTR_X86_SSE_UCOMILT_SS            = 832
INTR_X86_SSE_UCOMINEQ_SS           = 833
INTR_X86_SSSE3_PABS_B              = 834
INTR_X86_SSSE3_PABS_B_128          = 835
INTR_X86_SSSE3_PABS_D              = 836
INTR_X86_SSSE3_PABS_D_128          = 837
INTR_X86_SSSE3_PABS_W              = 838
INTR_X86_SSSE3_PABS_W_128          = 839
INTR_X86_SSSE3_PHADD_D             = 840
INTR_X86_SSSE3_PHADD_D_128         = 841
INTR_X86_SSSE3_PHADD_SW            = 842
INTR_X86_SSSE3_PHADD_SW_128        = 843
INTR_X86_SSSE3_PHADD_W             = 844
INTR_X86_SSSE3_PHADD_W_128         = 845
INTR_X86_SSSE3_PHSUB_D             = 846
INTR_X86_SSSE3_PHSUB_D_128         = 847
INTR_X86_SSSE3_PHSUB_SW            = 848
INTR_X86_SSSE3_PHSUB_SW_128        = 849
INTR_X86_SSSE3_PHSUB_W             = 850
INTR_X86_SSSE3_PHSUB_W_128         = 851
INTR_X86_SSSE3_PMADD_UB_SW         = 852
INTR_X86_SSSE3_PMADD_UB_SW_128     = 853
INTR_X86_SSSE3_PMUL_HR_SW          = 854
INTR_X86_SSSE3_PMUL_HR_SW_128      = 855
INTR_X86_SSSE3_PSHUF_B             = 856
INTR_X86_SSSE3_PSHUF_B_128         = 857
INTR_X86_SSSE3_PSHUF_W             = 858
INTR_X86_SSSE3_PSIGN_B             = 859
INTR_X86_SSSE3_PSIGN_B_128         = 860
INTR_X86_SSSE3_PSIGN_D             = 861
INTR_X86_SSSE3_PSIGN_D_128         = 862
INTR_X86_SSSE3_PSIGN_W             = 863
INTR_X86_SSSE3_PSIGN_W_128         = 864
INTR_XCORE_BITREV                  = 865
INTR_XCORE_GETID                   = 866

