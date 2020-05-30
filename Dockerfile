FROM centos

RUN yum install python36 -y

RUN yum -y install epel-release

RUN yum -y install gcc gcc-c++ python-pip python-devel atlas atlas-devel gcc-gfortran openssl-devel libffi-devel

COPY  . .

RUN pip3 install --upgrade --no-cache-dir -r requirement_cnn.txt

CMD [ "mkdir", "/model_dir" ]

CMD [ "python3", "/model_dir/model_train.py" ]