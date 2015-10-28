import os
import sys

def filterbyvalue(seq, value):
   for el in seq:
       if value in el: yield el
#limitation on chronos, set environment on py
os.environ["AWS_ACCESS_KEY_ID"]= sys.argv[2]
os.environ["AWS_SECRET_ACCESS_KEY"]= sys.argv[3]
os.environ["BUCKET_NAME"]=sys.argv[4]
os.environ["AWS_DEFAULT_REGION"]=sys.argv[5]


def main():
    if (len(sys.argv) >= 7 and sys.argv[6] != 'upload'):
        print('upload init')
        i#part1 get file from s3 bucket
        __exec = call(['aws','s3','cp',sys.argv[1], str('s3://' + os.environ['BUCKET_NAME'] + '/' + sys.argv[1]) ])
    else:
        print('download init')
        #part1 get file from s3 bucket
        __exec = call(['aws','s3','cp',str('s3://' + os.environ['BUCKET_NAME'] + '/' + sys.argv[1]),'.'])



if __name__ == "__main__":
    main()
