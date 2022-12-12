# A3-GRPC
## 17625 - Api Design Assignment
Created by : Jyot Ashwin Mehta (jyotashm)

All the protos are present in the `protos` directory.
All the generated 'pb2' files are present in `service` directory.


To generate the code for proto files, follow below commands:

```shell

cd protos
python -m grpc_tools.protoc -I. --python_out=../service --pyi_out=../service --grpc_python_out=../service *service.proto
python -m grpc_tools.protoc -I. --python_out=../service --pyi_out=../service  *entities.proto
```

After running these commands, there will be 'pb2' files in the `service` directory.
To start the python server:
- Open `inventory_service_pb2.py`.
- Change
   ```python
     import library_entities_pb2 as library__entities__pb2
   ```  
    to
    ```python 
       from . import library_entities_pb2 as library__entities__pb2
    ```
- Open `inventory_service_pb2_grpc.py`.
- Change
   ```python
    import inventory_service_pb2 as inventory__service__pb2
   ```  
    to
    ```python 
      from . import inventory_service_pb2 as inventory__service__pb2
    ```
- Run this command:
    ```shell
    cd ..
    python .\inventory_server.py
  ```

- The log should say: `Server started listening at: localhost:50051
`
