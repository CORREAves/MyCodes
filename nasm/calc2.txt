%include "io.inc"
section .data
    ;declara a string
    entrada db "751 2 +", 0ah
    entrlen equ $-entrada
    fimdastring db 0 ;será usado para controlar o fim da string no prefixo
    contador db -1
section .text
global CMAIN
CMAIN:
    mov ebp, esp; for correct debugging
    ;limpar registradores
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx
    xor edi, edi
    xor esi, esi
    ; mover a string pro registrador e edi
    mov esi, entrada
    ; executa comparação para ir a prefixa ou posfixa
    cmp byte [esi], 48
    jge posfixa
    mov [fimdastring], esi
    jnge revertstring 
    
    
posfixa:
    cmp byte [esi], 0ah
    je fim
    
    cmp byte [esi], 32
    je ignoraespacopos
    
    cmp byte [esi], 48
    jge empilhanumeropos
    jnge fazoperacaopos
     
empilhanumeropos:
    inc esi
    cmp byte [esi], 32
    jne dezena
    dec esi
    PRINT_DEC 1, [esi]
    NEWLINE
    sub byte [esi], 48
    PRINT_DEC 1, [esi]
    NEWLINE
    lodsb
    PRINT_DEC 1, eax
    NEWLINE
    push eax
    xor eax, eax
    xor ebx, ebx
    jmp posfixa
    
dezena:
    inc esi
    cmp byte [esi], 32
    jne milhar
    dec esi
    PRINT_DEC 1, [esi]
    NEWLINE
    sub byte [esi], 48
    PRINT_DEC 1, [esi]
    NEWLINE
    lodsb
    PRINT_DEC 1, eax
    NEWLINE
    mov bl, al
    xor eax, eax
    dec esi
    dec esi
    PRINT_DEC 1, [esi]
    NEWLINE
    sub byte [esi], 48
    PRINT_DEC 1, [esi]
    NEWLINE
    lodsb
    PRINT_DEC 1, eax
    NEWLINE
    mov cl, 10
    mul cl
    add al, bl
    PRINT_DEC 1, eax
    NEWLINE
    push eax
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    inc esi
    jmp posfixa

milhar:
    sub byte [esi], 48
    lodsb
    PRINT_DEC 1, eax
    NEWLINE
    mov cx, ax
    PRINT_DEC 1, ecx
    NEWLINE
    PRINT_DEC 1, eax
    NEWLINE
    xor eax, eax
    dec esi
    dec esi
    PRINT_DEC 1, [esi]
    NEWLINE
    sub byte [esi], 48
    lodsb
    PRINT_DEC 1, eax
    NEWLINE
    mov dx, 10
    mul dx
    PRINT_DEC 1, eax
    NEWLINE
    add ax, cx
    PRINT_DEC 1, eax
    NEWLINE    
    mov cx, ax
    PRINT_DEC 1, ecx
    NEWLINE
    xor eax, eax
    dec esi
    dec esi
    PRINT_DEC 1, [esi]
    NEWLINE
    sub byte [esi], 48
    lodsb
    PRINT_DEC 1, eax
    NEWLINE
    mov bx, 100
    mul bx
    add ax, cx
    PRINT_DEC 1, eax
    NEWLINE
    push eax
    xor eax, eax
    xor ebx, ebx
    xor edx, edx
    inc esi
    inc esi
    inc esi
    jmp posfixa
       
ignoraespacopos:
    inc esi
    jmp posfixa
        
fazoperacaopos:
    cmp byte [esi], '+'
    je somapos
    
    cmp byte [esi], '-'
    je subtracaopos
    
    cmp byte [esi], '*'
    je multiplicacaopos
    
    cmp byte [esi], '/'
    je divisaopos
    
somapos:
    xor eax, eax
    xor ebx, ebx
    pop ebx
    pop eax
    PRINT_DEC 4, ebx
    NEWLINE
    PRINT_DEC 4, eax
    NEWLINE
    add eax, ebx
    PRINT_DEC 4, eax
    push eax
    xor eax, eax
    xor ebx, ebx
    inc esi
    jmp posfixa
    
subtracaopos:
    pop ebx
    pop eax
    sub eax, ebx
    push eax
    xor eax, eax
    xor ebx, ebx
    inc esi
    jmp posfixa
       
multiplicacaopos:
    pop ecx
    pop eax
    mul ecx
    push eax
    xor eax, eax
    xor ecx, ecx
    inc esi
    jmp posfixa
       
divisaopos:
    pop ecx
    pop eax
    div ecx
    push ecx
    xor eax, eax
    xor ecx, ecx
    inc esi
    jmp posfixa
  
    
revertstring:
    cmp byte [esi], 0ah
    jne passastring
    je fiminicio
    
passastring:
    inc esi
    jmp revertstring
          
fiminicio:
    dec esi
    jmp prefixa
          
prefixa:
    ;cmp  [fimdastring], esi
    ;je fim
    
    cmp byte [esi], 32
    je ignoraespacopre
    
    cmp byte [esi], 48
    jge empilhanumeropre
    jnge fazoperacaopre            
              
empilhanumeropre:
    mov ebx, esi
    sub byte [esi], 48
    lodsb
    mov esi, ebx
    push eax
    xor eax, eax
    xor ebx, ebx
    dec esi
    jmp prefixa                

ignoraespacopre:
    dec esi
    jmp prefixa

fazoperacaopre:
    cmp byte [esi], '+'
    je somapre
    
    cmp byte [esi], '-'
    je subtracaopre
    
    cmp byte [esi], '*'
    je multiplicacaopre
    
    cmp byte [esi], '/'
    je divisaopre

somapre:
    pop ebx
    pop eax
    PRINT_DEC 1, [ebx]
    NEWLINE
    PRINT_DEC 1, [eax]
    NEWLINE
    add eax, ebx
    PRINT_DEC 1, [eax]
    push eax
    xor eax, eax
    xor ecx, ecx
    cmp  [fimdastring], esi
    je fim
    dec esi
    jmp prefixa

subtracaopre:
    pop ebx
    pop eax
    sub eax, ebx
    push eax
    xor eax, eax
    xor ebx, ebx
    cmp  [fimdastring], esi
    je fim
    dec esi
    jmp prefixa

multiplicacaopre:
    pop ecx
    pop eax
    mul ecx
    push ecx
    xor eax, eax
    xor ecx, ecx
    cmp  [fimdastring], esi
    je fim
    dec esi
    jmp prefixa                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

divisaopre:
    pop ecx
    pop eax
    div ecx
    push ecx
    xor eax, eax
    xor ecx, ecx
    cmp  [fimdastring], esi
    je fim
    dec esi
    jmp prefixa                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
fim:
    xor ebx, ebx
    pop ebx
    PRINT_DEC 1, ebx

    ret    
    
    
    
    
    ;PRINT_DEC 1, [edi]
    
    
    ret
    
;prefixa:
    ;PRINT_DEC 1, [edi]
    
    
    ret