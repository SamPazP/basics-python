
def hello_word():
    print("Hello, word!")


def hello_word_name(first_name):
    print(f"Hello, {first_name}")


def hello_word_args(*args):
    first_name = args[0]
    second_name = args[1]
    third_name = args[2]


    #print(args)
    #print(type(args))
    #print("Hello, Args!")
    #print(first_name)

    #print(f"Hello, {first_name}/{second_name}/{third_name}!")

def hello_word_keyword_args(first_pesron,second_person):
    print(f"Hello, {first_pesron} / {second_person}")

#hello_word_keyword_args(first_pesron="Sebastian",second_person="Daniel")

def hello_world_arbitrary_keyword_args(**kwargs):
    #print(kwargs)
    #print(type(kwargs))
    #print(kwargs.get('second_person'))
    #print(kwargs.get('first_person'))
    if kwargs.get('second_person') is None:
        print ('No hay segunda persona')
    else:
        print(f"Hello, {kwargs['first_person']}/{kwargs['second_person']} ! ")
    

hello_world_arbitrary_keyword_args(first_person="Vanessa",second_person="Jose")
hello_world_arbitrary_keyword_args(first_person='Vanessa')


#hello_word()
#hello_word_name("Samantha")
#hello_word_args("Sebastian", "Daniel", "Vanessa")

