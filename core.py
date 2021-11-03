class Codehandler:

    def move_handler(registers):
        reg_left, reg_right = registers.split(",")

        if reg_left =="b":
            code_data = {
            "b" : "40",
            "c" : "41",
            "d" : "42",
            "e" : "43",
            "h" : "44",
            "l" : "45",
            "m" : "46",
            "a" : "47"
            }
            return code_data[reg_right]

        if reg_left =="c":
            code_data = {
            "b" : "48",
            "c" : "49",
            "d" : "4a",
            "e" : "4b",
            "h" : "4c",
            "l" : "4d",
            "m" : "4e",
            "a" : "4f"
            }
            return code_data[reg_right]

        if reg_left =="d":
            code_data = {
            "b" : "50",
            "c" : "51",
            "d" : "52",
            "e" : "53",
            "h" : "54",
            "l" : "55",
            "m" : "56",
            "a" : "57"
            }
            return code_data[reg_right]

        if reg_left =="e":
            code_data = {
            "b" : "58",
            "c" : "59",
            "d" : "5a",
            "e" : "5b",
            "h" : "5c",
            "l" : "5d",
            "m" : "5e",
            "a" : "5f"
            }
            return code_data[reg_right]

        if reg_left =="h":
            code_data = {
            "b" : "60",
            "c" : "61",
            "d" : "62",
            "e" : "63",
            "h" : "64",
            "l" : "65",
            "m" : "66",
            "a" : "67"
            }
            return code_data[reg_right]

        if reg_left =="l":
            code_data = {
            "b" : "68",
            "c" : "69",
            "d" : "6a",
            "e" : "6b",
            "h" : "6c",
            "l" : "6d",
            "m" : "6e",
            "a" : "6f"
            }
            return code_data[reg_right]

        if reg_left =="m":
            code_data = {
            "b" : "70",
            "c" : "71",
            "d" : "72",
            "e" : "73",
            "h" : "74",
            "l" : "75",
            "m" : "76",
            "a" : "77"
            }
            return code_data[reg_right]

        if reg_left =="a":
            code_data = {
            "b" : "78",
            "c" : "79",
            "d" : "7a",
            "e" : "7b",
            "h" : "7c",
            "l" : "7d",
            "m" : "7e",
            "a" : "7f"
            }
            return code_data[reg_right]

    #leftmost part
    def add_handler(register):
        code_data = {
            "b" : "80",
            "c" : "81",
            "d" : "82",
            "e" : "83",
            "h" : "84",
            "l" : "85",
            "m" : "86",
            "a" : "87"
        }
        return code_data[register]
    
    def adc_handler(register):
        code_data = {
            "b" : "88",
            "c" : "89",
            "d" : "8a",
            "e" : "8b",
            "h" : "8c",
            "l" : "8d",
            "m" : "8e",
            "a" : "8f"
        }
        return code_data[register]
    
    def sub_handler(register):
        code_data = {
            "b" : "90",
            "c" : "91",
            "d" : "92",
            "e" : "93",
            "h" : "94",
            "l" : "95",
            "m" : "96",
            "a" : "97"
        }
        return code_data[register]

    def sbb_handler(register):
        code_data = {
            "b" : "98",
            "c" : "99",
            "d" : "9a",
            "e" : "9b",
            "h" : "9c",
            "l" : "9d",
            "m" : "9e",
            "a" : "9f"
        }
        return code_data[register]
    def ana_handler(register):
        code_data = {
            "b" : "a0",
            "c" : "a1",
            "d" : "a2",
            "e" : "a3",
            "h" : "a4",
            "l" : "a5",
            "m" : "a6",
            "a" : "a7"
        }
        return code_data[register]

    def xra_handler(register):
        code_data = {
            "b" : "a8",
            "c" : "a9",
            "d" : "aa",
            "e" : "ab",
            "h" : "ac",
            "l" : "ad",
            "m" : "ae",
            "a" : "af"
        }
        return code_data[register]

    def ora_handler(register):
        code_data = {
            "b" : "b0",
            "c" : "b1",
            "d" : "b2",
            "e" : "b3",
            "h" : "b4",
            "l" : "b5",
            "m" : "b6",
            "a" : "b7"
        }
        return code_data[register]

    def cmp_handler(register):
        code_data = {
            "c" : "b8",
            "d" : "b9",
            "e" : "ba",
            "h" : "bb",
            "l" : "bc",
            "b" : "bd",
            "m" : "be",
            "a" : "bf"
        }
        return code_data[register]

    def inr_handler(register):
        code_data = {
            "b" : "04",
            "c" : "0c",
            "d" : "14",
            "e" : "1c",
            "h" : "24",
            "l" : "2c",
            "m" : "34",
            "a" : "3c"
        }
        return code_data[register]

    def dcr_handler(register):
        code_data = {
            "b" : "05",
            "c" : "0d",
            "d" : "15",
            "e" : "1d",
            "h" : "25",
            "l" : "2d",
            "m" : "35",
            "a" : "3d"
        }
        return code_data[register]

    def mvi_handler(register):
        code_data = {
            "b" : "06",
            "c" : "0e",
            "d" : "16",
            "e" : "1e",
            "h" : "26",
            "l" : "2e",
            "m" : "36",
            "a" : "3e"
        }
        return code_data[register]


    
    #top left
    def lxi_handler(register):
        code_data = {
            "b" : "01",
            "d" : "11",
            "h" : "21",
            "sp": "31"
        }
        return code_data[register]

    def inx_handler(register):
        code_data = {
            "b" : "03",
            "d" : "13",
            "h" : "23",
            "sp": "33"
        }
        return code_data[register]

    def dcx_handler(register):
        code_data = {
            "b" : "0b",
            "d" : "1b",
            "h" : "2b",
            "sp": "3b"
        }
        return code_data[register]

    def dad_handler(register):
        code_data = {
            "b" : "09",
            "d" : "19",
            "h" : "29",
            "sp": "39"
        }
        return code_data[register]

    def ldax_handler(register):
        code_data = {
            "b" : "0a",
            "d" : "1a"
        }
        return code_data[register]

    def stax_handler(register):
        code_data = {
            "b" : "02",
            "d" : "12",
            "sp": "psw"
        }
        return code_data[register]

    def push_handler(register):
        code_data = {
            "b" : "c5",
            "d" : "d5",
            "h" : "e5",
            "sp": "f5"
        }
        return code_data[register]

    def pop_handler(register):
        code_data = {
            "b" : "c1",
            "d" : "d1",
            "h" : "e1",
            "sp": "f1"
        }
        return code_data[register]

    def rst_handler(register):
        code_data = {
            "0" : "c7",
            "1" : "cf",
            "2" : "d7",
            "3" : "df",
            "4" : "e7",
            "5" : "ef",
            "6" : "f7",
            "7" : "ff"
        }
        return code_data[register]

    def jmp_handler(register_address,label_list):
        code_data = {
            "jmp" : "c3",
            "jz" : "ca",
            "jnz" : "c2",
            "jc" : "da",
            "jnc" : "d2",
            "jpe" : "ea",
            "jpo" : "e2",
            "jm" : "fa",
            "jp" : "f2"
        }
        for keys in code_data:
            if register_address.startswith(keys):
                register_address = register_address.replace(keys,"")
                try:
                    register_address = hex(label_list[register_address] )
                    register_address = register_address.replace("0x","")
                    return [code_data[keys],register_address[len(register_address)//2:],register_address[:len(register_address)//2]]
                except:
                    return [code_data[keys],f"{register_address}",f"{register_address}"]
def transpile(code:str,load_location):
    load_location = int(load_location,base=16)
    code = code.replace("\t","")
    code = code.replace(" ","")
    code = code.lower()
    code = code.split("\n")

    label_dict = {}
    hex_list = []

    for line in code:
       
        line = line.split(";")[0]

        #labels 
        if ":" in line:
            label = line.split(":")[0]
            next_index =int(load_location) + len(hex_list)
            label_dict[label] = next_index

        #move handler

        if "mov" in line:
            line = line.replace("mov","")
            hex_list.append(Codehandler.move_handler(line))

        #left most part
        if "add" in line:
            line = line.replace("add","")
            hex_list.append(Codehandler.add_handler(line))

        if "adc" in line:
            line = line.replace("adc","")
            hex_list.append(Codehandler.adc_handler(line))
        
        if "sub" in line:
            line = line.replace("sub","")
            hex_list.append(Codehandler.sub_handler(line))

        if "sbb" in line:
            line = line.replace("sbb","")
            hex_list.append(Codehandler.sbb_handler(line))

        if "ana" in line:
            line = line.replace("ana","")
            hex_list.append(Codehandler.ana_handler(line))

        if "xra" in line:
            line = line.replace("xra","")
            hex_list.append(Codehandler.xra_handler(line))

        if "ora" in line:
            line = line.replace("ora","")
            hex_list.append(Codehandler.ora_handler(line))

        if "cmp" in line:
            line = line.replace("cmp","")
            hex_list.append(Codehandler.cmp_handler(line))
                
        if "inr" in line:
            line = line.replace("inr","")
            hex_list.append(Codehandler.inr_handler(line))

        if "dcr" in line:
            line = line.replace("dcr","")
            hex_list.append(Codehandler.dcr_handler(line))

        if "mvi" in line:
            line = line.replace("mvi","")
            command,location = line.split(",")
            hex_list.append(Codehandler.mvi_handler(command))
            location = location.replace("h","")
            hex_list.append(location)    #lower byte lower address


        #top left
        if "lxi" in line:
            line = line.replace("lxi","")
            line = line.split(",")
            command = line[0]
            location = line[1]
            hex_list.append(Codehandler.lxi_handler(command))
            location = location.replace("h","")
            hex_list.append(location[len(location)//2:])    #lower byte lower address
            hex_list.append(location[:len(location)//2])    # higher byte higher addres

        if "inx" in line:
            line = line.replace("inx","")
            hex_list.append(Codehandler.inx_handler(line))

        if "dcx" in line:
            line = line.replace("dcx","")
            hex_list.append(Codehandler.dcx_handler(line))

        if "dad" in line:
            line = line.replace("dad","")
            hex_list.append(Codehandler.dad_handler(line))
        
        if "ldax" in line:
            line = line.replace("ldax","")
            hex_list.append(Codehandler.ldax_handler(line))
        
        if "stax" in line:
            line = line.replace("stax","")
            
            hex_list.append(Codehandler.stax_handler(line))
            
        if "push" in line:
            line = line.replace("push","")
            hex_list.append(Codehandler.push_handler(line))
        
        if "pop" in line:
            line = line.replace("pop","")
            hex_list.append(Codehandler.pop_handler(line))
            

        
        #reset
        if "rst" in line:
            line = line.replace("rst","")
            hex_list.append(Codehandler.rst_handler(line))


        #loners
        if "hlt" in line:
            hex_list.append("76")
        
        if "nop" in line:
            hex_list.append("00")
        
        if "rim" in line:
            hex_list.append("20")
        
        if "sim" in line:
            hex_list.append("30")

        if "ei" in line:
            hex_list.append("fb")

        if "di" in line:
            hex_list.append("f3")

        if "in" in line:
            hex_list.append("db")

        if "out" in line:
            hex_list.append("d3")

        if "lhld" in line:
            hex_list.append("2a")
        
        if "shld" in line:
            line = line.replace("shld","")
            hex_list.append("22")
            line = line.replace("h","")
            hex_list.append(line[len(line)//2:])    #lower byte lower address
            hex_list.append(line[:len(line)//2])

        
        if "lda" in line:
            hex_list.append("3a")
        
        if "xchg" in line:
            hex_list.append("eb")

        if "xthl" in line:
            hex_list.append("e3")
        
        if "pchl" in line:
            hex_list.append("e9")
        
        if "sphl" in line:
            hex_list.append("f9")

        if "sta" in line:
            line = line.replace("sta","")
            hex_list.append("32")
            line = line.replace("h","")
            hex_list.append(line[len(line)//2:])    #lower byte lower address
            hex_list.append(line[:len(line)//2])
            

        if "j" in line:
            hex_list.extend(Codehandler.jmp_handler(line,label_dict))



    for code in hex_list:
        if code in label_dict.keys():
            address = label_dict[code]
            address = hex(address)
            address = address.replace("0x","")
            index = hex_list.index(code)
            hex_list[index] = address[len(address)//2:]
            hex_list[index+1] = address[:len(address)//2]
    return hex_list
