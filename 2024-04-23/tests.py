from funcoes import conversor_temperatura

def test_conversor_temperatura():
    input_caso1 = -273.15
    input_caso2 = -173.15
    
    expected_caso1 = 0
    expected_caso2 = 100

    result_1 = conversor_temperatura(input_caso1, "C", "K")
    result_2 = conversor_temperatura(input_caso2, "C", "K")
    

    assert result_1 == expected_caso1
    assert result_2 == expected_caso2
    

def test_conversor_temperatura_fails():
        input_caso3 = 0
        expected_caso3 = 273.15
        result_3 = conversor_temperatura(input_caso3, "C", "K")
        assert result_3 == expected_caso3