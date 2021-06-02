def f(x,y,z,a=1,b=2):
    print("x="+str(x)+"y="+str(y)+"z="+str(z)+" op引数:"+str(a)+","+str(b))
    
a,b,c = map(int,input("3桁の数字を半角スペースを開けて入力").split())

f(a,b,c)