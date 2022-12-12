# A3-GRPC
## 17625 - Api Design Assignment
Created by : Jyot Ashwin Mehta (jyotashm)

To generate the code for proto files, follow below commands:

```shell

cd src/protos
python -m grpc_tools.protoc -I. --python_out=../service --pyi_out=../service --grpc_python_out=../service *service.proto
python -m grpc_tools.protoc -I. --python_out=../service ==pyi_out=../service  *entities.proto
```

