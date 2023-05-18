import requests,time,sys,os

def main():
    Led='https://navlab.ericroy.net/led'
    Pot='https://navlab.ericroy.net/potenciometre'
    while(True):
        r = requests.get(Led)
        if r.status_code==200:
            p = requests.post(Led,json=r.json())
            if p.status_code!=204:
                print('Bad response for POST to',Led,'Status code:',p.status_code)
        else:
            print('Bad response for GET to',Led,'Status code:',r.status_code)
        r = requests.get(Pot)
        if r.status_code==200:
            p = requests.post(Pot,json=r.json())
            if p.status_code!=204:
                print('Bad response for POST to',Pot,'Status code:',p.status_code)
        else:
            print('Bad response for GET to',Pot,'Status code:',r.status_code)
        time.sleep(5)
    

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
