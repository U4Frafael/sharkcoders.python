dias = input("Que dia deseja verificar?: ")

match dias:
    case 'Segunda':
        print("Começa a semana com exercício físico. ")
    case 'Terça':
        print("Participa em reuniões de equipa.")
    case 'Quarta':
        print("Trabalha nas tarefas do projeto.")
    case 'Quinta':
        print("Planeia a semana seguinte. ")
    case 'Sexta':
        print("Conclui o trabalho e relaxa.")
    case 'Sábado':
        print("Desfruta de atividades de lazer.")
    case 'Domingo':
        print("Descansa e recarrega energias para a próxima semana. ")
    case _:
        print("Dia inválido")