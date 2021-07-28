	.file	"ejemplito.c"
	.text
	.globl	cad1
	.section	.rodata
.LC0:
	.string	"\302\241Hola mundo!\n"
	.section	.data.rel.local,"aw"
	.align 8
	.type	cad1, @object
	.size	cad1, 8
cad1:
	.quad	.LC0
	.globl	cad2
	.section	.rodata
.LC1:
	.string	"... Mundo inmundo... \n"
	.section	.data.rel.local
	.align 8
	.type	cad2, @object
	.size	cad2, 8
cad2:
	.quad	.LC1
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	$0, -4(%rbp)
	movq	cad1(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movq	cad2(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Debian 10.2.1-6) 10.2.1 20210110"
	.section	.note.GNU-stack,"",@progbits
