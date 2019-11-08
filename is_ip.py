#判断ip地址是否合法
#192.168.1.1
def ip(ipstr):
    iplist=ipstr.split('.')
    if len(iplist)!=4:
        return "ip地址长度不是4"
    for i in range(len(iplist)):
        if iplist[i].isdigit()==False:
            return 'ip地址不全是数字'
        iplist[i]=int(iplist[i])
        if iplist[i]<=255 and iplist[i]>=0:
            pass
        else:
            return ("请检查ip地址,ip不在0-255之间")
            break
    return "{}是合法的地址".format(ipstr)
ipresult=ip('192.168.1.-1')
print(ipresult)
