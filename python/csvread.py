import pandas as pd

def get_csv(filename,column):
    df = pd.read_csv(filename)
    print(df)
    print(df.columns)
    
    ls=df[column].to_list()
    #print(ls_jinkou)
    return ls


if __name__ == "__main__":
    ls_nenrei=get_csv("jinkou.csv","nenrei")
    print("The list content of nenrei is below\n",ls_nenrei)
    ls_jinkou=get_csv("jinkou.csv","jinkou")
    print("The list content of jinkou is below\n",ls_jinkou)

    sum=0
    total_jinkou=0
    saikoubi=len(ls_jinkou)
    for i in range(saikoubi):
        print(ls_nenrei[i],ls_jinkou[i])
        sum+=(ls_nenrei[i]*ls_jinkou[i])
        total_jinkou+=ls_jinkou[i]
    print("sum=",sum,"  total=",total_jinkou)
    avg=sum/total_jinkou
    print(avg)
    
   

