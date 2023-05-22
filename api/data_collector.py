import requests,time,sys,os

def main():
    Site='https://navlab.ericroy.net'
    Led=Site+'/led'
    Pot=Site+'/potenciometre'
    while(True):
        try:
            r = requests.get(Led)
        except:
            print('Failed to establish a new connection with',Site)
        else:
            if r.status_code==200:
                try:
                    p = requests.post(Led,json=r.json())
                except:
                    print('Failed to establish a new connection with',Site)
                else:
                    if p.status_code!=204:
                        print('Bad response for POST to',Led,'| Status code:',p.status_code)
            else:
                print('Bad response for GET to',Led,'| Status code:',r.status_code)
        try:
            r = requests.get(Pot)
        except:
            print('Failed to establish a new connection with',Site)
        else:
            if r.status_code==200:
                try:
                    p = requests.post(Pot,json=r.json())
                except:
                    print('Failed to establish a new connection with',Site)
                else:
                    if p.status_code!=204:
                        print('Bad response for POST to',Pot,'| Status code:',p.status_code)
            else:
                print('Bad response for GET to',Pot,'| Status code:',r.status_code)
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
