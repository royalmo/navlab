import requests,time,sys,os,datetime

def main():
    serial_site='http://serial.navlab.ericroy.net'
    db_site='http://db.navlab.ericroy.net'
    while(True):
        try:
            r = requests.get(f"{serial_site}/led")
        except:
            print('Failed to establish a new connection with',serial_site)
        else:
            if r.status_code==200:
                try:
                    d=r.json()
                    d['time']=str(datetime.datetime.now())
                    p = requests.post(f"{db_site}/led",json=d)
                except:
                    print('Failed to establish a new connection with',db_site)
                else:
                    if p.status_code!=204:
                        print('Bad response for POST to',db_site,'| Status code:',p.status_code)
            else:
                print('Bad response for GET to',serial_site,'| Status code:',r.status_code)
        try:
            r = requests.get(f"{serial_site}/potenciometre")
        except:
            print('Failed to establish a new connection with',serial_site)
        else:
            if r.status_code==200:
                try:
                    d=r.json()
                    d['time']=str(datetime.datetime.now())
                    p = requests.post(f"{db_site}/potenciometre",json=d)
                except:
                    print('Failed to establish a new connection with',db_site)
                else:
                    if p.status_code!=204:
                        print('Bad response for POST to',db_site,'| Status code:',p.status_code)
            else:
                print('Bad response for GET to',serial_site,'| Status code:',r.status_code)
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
