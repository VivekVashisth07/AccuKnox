
import ast
def func(url):
    # reading the file
    files = open(url, 'r')
    Lines = files.read().splitlines()
    files.close()
    data_dict=dict()
    for i in Lines:
        if i:
            if Lines.count(i)==1:
                d=ast.literal_eval(i.split(": ")[1])
                if data_dict.get(d[1]):
                    data_dict[d[1]]+=[d[0]]
                else:
                    data_dict[d[1]]=[d[0]]
            else:
                return "Error: Repeated Data"
    data_dict= {i:data_dict[i] for i in sorted(data_dict,key=lambda i:len(data_dict[i]),reverse=True)}
    result=list(data_dict.keys())
    return ", ".join(result[:3])

if __name__=="__main__":
    url=input()
    print(func(url))
