FROM centos

COPY Dockerfile/ /model_dir/

RUN yum install python36 -y

RUN yum -y install epel-release

RUN pip3 install --upgrade pip

RUN pip3 install --upgrade --no-cache-dir -r requirement_cnn.txt

CMD [ "mkdir", "/model_dir" ]

CMD [ "python3", "/model_dir/model_train.py" ]