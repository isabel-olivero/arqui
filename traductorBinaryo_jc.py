hexatobin = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111"
}

bintohexa = {
    "0000": '0',
    "0001": '1',
    "0010": '2',
    "0011": '3',
    "0100": '4',
    "0101": '5',
    "0110": '6',
    "0111": '7',
    "1000": '8',
    "1001": '9',
    "1010": 'A',
    "1011": 'B',
    "1100": 'C',
    "1101": 'D',
    "1110": 'E',
    "1111": 'F'
}

MipsRHexa = {
    "100000": "20",
    "100001": "21",
    "100100": "24",
    "001000": "08",
    "100101": "25",
    "101010": "2a",
    "101011": "2b",
    "000000": "00",
    "000010": "02",
    "100010": "22",
    "100011": "23"
}

registros = {
    "$zero": "00000",
    "$at": "00001",
    "$v0": "00010",
    "$v1":"00011",
    "$a0": "00100",
    "$a1": "00101",
    "$a2": "00110",
    "$a3": "00111",
    "$t0": "01000",
    "$t1": "01001",
    "$t2": "01010",
    "$t3": "01011",
    "$t4": "01100",
    "$t5": "01101",
    "$t6": "01110",
    "$t7": "01111",
    "$s0": "10000",
    "$s1": "10001",
    "$s2": "10010",
    "$s3": "10011",
    "$s4": "10100",
    "$s5": "10101",
    "$s6": "10110",
    "$s7": "10111",
    "$t8": "11000",
    "$t9": "11001",
    "$k0": "11010",
    "$k1": "11011",
    "$gp": "11100",
    "$sp": "11101",
    "$fp": "11110",
    "$ra": "11111",
    "addi": "001000",
    "add": "100000",
    "lw": "100011",
    "sw": "101011",
    "sub": "100010",
    "mult": "011000",
    "multu": "011001",
    "mfhi": "010000",
    "mflo": "010010",
    "div": "011010",
    "lui": "001111",
    "ori": "001101",
    "beq": "000100",
    "bne": "000101",
    "j": "000010",
    "jal": "000011",
    "jr": "001000",
    "slt": "101010",
    "addiu": "001000",
    "addu": "100001",
    "andi": "001100",
    "lbu": "100100",
    "lhu": "100101",
    "ll": "110000",
    "slti": "001010",
    "sltiu": "001011",
    "sltu": "101011",
    "sll": "000000",
    "srl": "000010",
    "sb": "101000",
    "sc": "111000",
    "sh": "101001",
    "subu": "100011",
    "and": "100100",
    "or": "100101",
    "nor": "100111",
    "divu": "011011"
}

binregistro= {
    "00000": "$zero",
    "00001": "$at",
    "00010": "$v0",
    "00011": "$v1",
    "00100": "$a0",
    "00101": "$a1",
    "00110": "$a2",
    "00111": "$a3",
    "01000": "$t0",
    "01001": "$t1",
    "01010": "$t2",
    "01011": "$t3",
    "01100": "$t4",
    "01101": "$t5",
    "01110": "$t6",
    "01111": "$t7",
    "10000": "$s0",
    "10001": "$s1",
    "10010": "$s2",
    "10011": "$s3",
    "10100": "$s4",
    "10101": "$s5",
    "10110": "$s6",
    "10111": "$s7",
    "11000": "$t8",
    "11001": "$t9",
    "11010": "$k0",
    "11011": "$k1",
    "11100": "$gp",
    "11101": "$sp",
    "11110": "$fp",
    "11111": "$ra",
    "001000": "addi",
    "100000": "add",
    "100011": "lw",
    "101011": "sw",
    "100010": "sub",
    "011000": "mult",
    "011001": "multu",
    "010000": "mfhi",
    "010010": "mflo",
    "011010": "div",
    "001111": "lui",
    "001101": "ori",
    "000100": "beq",
    "000101": "bne",
    "000010": "j",
    "000011": "jal",
    "001000": "jr",
    "101010": "slt",
    "001100": "addiu",
    "100001": "addu",
    "001100": "andi",
    "100100": "lbu",
    "100101": "lhu",
    "110000": "ll",
    "001010": "slti",
    "001011": "sltiu",
    "101011": "sltu",
    "000000": "sll",
    "000010": "srl",
    "101000": "sb",
    "111000": "sc"}


def mips_to_binary(instruction, opcode_dict):
    parts = instruction.replace(",", "").split()

    if len(parts) < 4:
        print("Error: Instrucción no válida.")
        return None

    opcode = parts[0]
    if opcode not in opcode_dict:
        print(f"Error: Opcode desconocido - {opcode}")
        return None
    
    opc = opcode_dict[opcode]

    rs = format(int(parts[3][2:]), '05b')  

    binary_representation = f'{opc}{rs}{rt}{rd}00000100000' 
    return binary_representation

opcode_dict = {
    'add': '000000',
}

while True:
    mips_instruction = input("Ingrese la instrucción MIPS (o escriba 'salir' para terminar): ")
    
    if mips_instruction.lower() == 'salir':
        print("Saliendo del programa.")
        break
    binary_code = mips_to_binary(mips_instruction, opcode_dict)
    if binary_code is not None:
        print(f"La instrucción MIPS: {mips_instruction}\nCódigo binario: {binary_code}")

