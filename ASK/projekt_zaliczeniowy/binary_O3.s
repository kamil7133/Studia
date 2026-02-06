	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 26, 0	sdk_version 26, 1
	.globl	_binary_search                  ; -- Begin function binary_search
	.p2align	2
_binary_search:                         ; @binary_search
	.cfi_startproc
; %bb.0:
	tbnz	w1, #31, LBB0_4
; %bb.1:
	mov	w9, #0                          ; =0x0
LBB0_2:                                 ; =>This Inner Loop Header: Depth=1
	add	w8, w1, w9
	lsr	w8, w8, #1
	ldr	w10, [x0, w8, uxtw #2]
	cmp	w10, w2
	b.eq	LBB0_5
; %bb.3:                                ;   in Loop: Header=BB0_2 Depth=1
	sub	w11, w8, #1
	cmp	w10, w2
	csel	w1, w11, w1, gt
	csinc	w9, w9, w8, gt
	cmp	w9, w1
	b.le	LBB0_2
LBB0_4:
	mov	w8, #-1                         ; =0xffffffff
LBB0_5:
	mov	x0, x8
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	mov	w8, #0                          ; =0x0
	mov	w9, #7                          ; =0x7
Lloh0:
	adrp	x10, l___const.main.tab@PAGE
Lloh1:
	add	x10, x10, l___const.main.tab@PAGEOFF
LBB1_1:                                 ; =>This Inner Loop Header: Depth=1
	add	w11, w8, w9
	lsr	w11, w11, #1
	ldr	w12, [x10, w11, uxtw #2]
	cmp	w12, #6
	b.eq	LBB1_4
; %bb.2:                                ;   in Loop: Header=BB1_1 Depth=1
	sub	w13, w11, #1
	cmp	w12, #6
	csel	w9, w13, w9, gt
	csinc	w8, w8, w11, gt
	cmp	w8, w9
	b.le	LBB1_1
; %bb.3:
	mov	w11, #-1                        ; =0xffffffff
LBB1_4:
	sub	sp, sp, #32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	str	x11, [sp]
Lloh2:
	adrp	x0, l_.str@PAGE
Lloh3:
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	mov	w0, #0                          ; =0x0
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32
	ret
	.loh AdrpAdd	Lloh0, Lloh1
	.loh AdrpAdd	Lloh2, Lloh3
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__const
	.p2align	2, 0x0                          ; @__const.main.tab
l___const.main.tab:
	.long	1                               ; 0x1
	.long	2                               ; 0x2
	.long	3                               ; 0x3
	.long	4                               ; 0x4
	.long	5                               ; 0x5
	.long	6                               ; 0x6
	.long	7                               ; 0x7

	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"%d\n"

.subsections_via_symbols
