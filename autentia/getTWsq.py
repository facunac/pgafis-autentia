#!/usr/bin/env python

import pyhs2
import base64
import psycopg2
import binascii


class pgAfis:
    pg_connstr = "host='localhost' dbname='afis' user='autentia' password='_voyager.'"

    def __init__(self):
        print "Connecting to database\n	->%s" % (self.pg_connstr)

        self.conn = psycopg2.connect(self.pg_connstr)

        self.cursor = self.conn.cursor()
        print "Connected!\n"

    def close(self):
        print "Close....."
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def savefile(self,rut,dedo,wsq):
        print rut+"_"+str(dedo)+".hex"
        with open(rut+"_"+str(dedo)+".wsq", "w") as text_file:
            text_file.write(base64.b64decode(wsq))

    def add_finger(self,registrado,pais,rut,tecnologia,institucion,dedo,wsq):
        pIns = "insert into fingerprints (registrado,pais,id,tecnologia,institucion,dedo,wsq) values ('"+ registrado +"','"+ pais +"','"+ rut +"','"+ tecnologia +"','"+ institucion +"','"+ str(dedo) +"','"+ binascii.hexlify(base64.b64decode(wsq)) +"')"
        print "exec --> "+pIns
        self.cursor.execute(pIns)
        pUpd = "update fingerprints set mdt = mindt(wsq,true) where id='"+rut+"' and pais = '"+pais+"' and tecnologia = '"+tecnologia+"' and institucion = '"+institucion+"' and dedo = "+str(dedo)
#        self.cursor.execute(pUpd)

def main():
    pafis = pgAfis()

    with pyhs2.connect(host='172.16.207.15',
        port=21050,
        authMechanism="NOSASL",
        user='facuna',
        password='h2onvnat$',
        database='autentia') as conn:

        print "conecto"
        with conn.cursor() as cur:
            cur.execute("select registrado , pais, rut, tecnologia, institucion, dedo, concat( wsq, ws2 ) wsq from aut_twsq limit 10")

            print cur.getSchema()

            for i in cur.fetch():
                #pafis.add_finger(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                pafis.savefile(i[2],i[5],i[6])
        pafis.close()

if __name__ == "__main__":
	main()
