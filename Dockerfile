FROM centos

RUN yum install python36 -y

COPY  . .

RUN pip3 install --no-cache-dir -r requirement_cnn.txt

CMD [ "mkdir", "/model_dir" ]

CMD [ "python", "/model_dir/model_train.py" ]