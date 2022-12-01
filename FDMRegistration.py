def fdmRegistration(stream, trainee):
    dictionary_stream = {"Devops": 0, "Devs": 0, "Aws": 0, "DataEng": 0, "TechOps": 0}
    msg = ""
    if (stream == "5"):
        if(len(Devops) < 5):
            Devops.append(trainee)
            dictionary_stream = {"Devops": len(Devops)}
            print(dictionary_stream)
            print (Devops)
            print(trainee + " is enrolled in DevOps Stream ")
            a()
        else :
            print("Devops Stream is full..")
            a()
    elif (stream == "1"):
        if (len(Devs) < 5):
            Devs.append(trainee)
            dictionary_stream = {"Devs": len(Devs)}
            print(dictionary_stream)
            print(Devs)
            print(trainee + " is enrolled in Software Development Stream ")
            a()
        else:
            print("Software Development Stream is full..")
            a()
    elif (stream == "2"):
        if (len(Aws) < 5):
            Aws.append(trainee)
            dictionary_stream = {"Aws": len(Aws)}
            print(dictionary_stream)
            print(Aws)
            print(trainee + " is enrolled in Aws Stream ")
            a()
        else:
            print("Aws Stream is full..")
            a()
    elif (stream == "3"):
        if (len(DataEng) < 5):
            DataEng.append(trainee)
            dictionary_stream = {"Devs": len(DataEng)}
            print(dictionary_stream)
            print(DataEng)
            msg = trainee + " is enrolled in Data Engineering Stream "
            a()
        else:
            msg = "Data Engineering Stream is full.."
            a()
    else:
        if (len(TechOps) < 5):
            TechOps.append(trainee)
            dictionary_stream = {"TechOps": len(TechOps)}
            print(dictionary_stream)
            print(TechOps)
            msg = trainee + " is enrolled in Techops Stream "
            a()
        else:
            msg = "TechOps Stream is full.."
            a()
    return print(msg)


def removeTrainee(stream, trainee):
    return print("Trainee has drop the class")

def a():
        stream = input("Choose "
                       "[1] for Software Development "
                       "[2] for Aws "
                       "[3] for Data Engineering "
                       "[4] for TechOps  "
                       "[5] for DevOps : ")
        trainee = input("Enter your name : ")
        fdmRegistration(stream, trainee)


Devops = []
Devs = []
Aws = []
DataEng = []
TechOps = []
a()
