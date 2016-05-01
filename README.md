# EasyPlan

### Source Tree Setup

1. Open Source Tree.
2. Click the “+New Repository” on the top.
3. Choose “Clone from URL”.
4. Copy and paste “https://github.com/chenjienan/EasyPlan” into the Source URL. The Destination Path and Name will be automatically generated.
5. Click “Clone” and the local repo will be created.
6. Pull the source code from remote.

### VirtualEnv Setup Instruction

1. Pull source code from github
2. run command: virtualenv -p python3 EasyPlan
3. Set up Virtualenv in PyCharm->File->Default Settings->Project Interpretator. Select Setting ->Add Local, and then choose the path  ~EasyPlan/bin/python.

### Database Connection Instruction
1. Create a DB called “easyplan” in PostgreSQL
2. sudo ln -s /Library/PostgreSQL/9.5/lib/libssl.1.0.0.dylib /usr/local/lib
3. sudo ln -s /Library/PostgreSQL/9.5/lib/libcrypto.1.0.0.dylib /usr/local/lib
4. change the SQLALCHEMY_DATABASE_URI to r“postgresql://<username>:<password>@localhost/easyplan”in application.py
5. run database_config.py