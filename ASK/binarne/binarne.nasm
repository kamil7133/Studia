section .data
    a dq 2, 5, 8, 12, 16, 23, 38, 56, 72, 91 ;inicializacja tablicy (kazdy po 8 bajtow bo dq)
    n dq 10 ;ilosc elementow
    x dq 23 ;liczba ktorej szukamy

section .text
    global _start ; sekcja tekst, funkcja zaczyna sie od start

_start:
    xor r8, r8 ;r8 = 0, rejestr 8
    mov r9, [n] ; rejestr 9 to 10 czyli ilosc elemntow 
    dec r9 ;decrement (r9-1)=9

_loop: ; poczatek petli
    cmp r8, r9 ;compare r8 i r9
    jg _err ; jezeli greater czyli r8>r9 to funkcja _err
    lea rax, [r8 + r9]
    shr rax, 1 ;przesun bit o 1 czyli dzielenie przez 2 
    mov rdx, [a + rax * 8] ; move, idz do tablicy, przesun o "rax" elementow * 8 czyli kazdy po 8 bitow, wrzuc do rdx
    cmp rdx, [x] ; compare z x czyli 23
    je _exit_ok ;jump if equal, koniec
    jl _right ;jump if less z 23 czyli szukamy po prawej polowie
    lea r9, [rax - 1] ; jesli bylo wieksze to rax - 1 (przesuwamy prawa granice )
    jmp _loop ;rekurencja
_right: ; wywolywanie gdy srodek byl za maly
    lea r8, [rax + 1] ;lewy wskaznik +1 
    jmp _loop ; powrot do petli

_err:
    mov rdi, -1 ;-1 do rd1 
    jmp _end ;end

_exit_ok:
    mov rdi, rax ;zamien rdi z rax

_end:
    mov rax, 60 ; kod na wyjscie z programu
    syscall ;syscall czyli zakonczenie programu 
