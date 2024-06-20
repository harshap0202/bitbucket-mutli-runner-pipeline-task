# Bitbucket run pipeline step with 2 seperate runners

Objective of this task was to create a POC to test in bitbucket. A pipeline was to be made to check if running a step with 2 seperate runner could upload the output of both runners in seperate file.

## Prerequisites :
 - Bitbucket account
 - linux device / EC2 Instance for runners
 
## Steps :

### 1. Runner 1 and 2 Setup
 - Go to Bitbucket Home Page -> Settings -> Workspace Settings -> **Workspace Runners**
 - click on **add runner** and fill following details:
    - System and architecture - Linux Shell
    - Runner Name - [ runner name ]
    - Runners Labesl - self.hosted, linux-shell, [ runner name ]
 - click next and on next page a list of commands is given to setup runner in linux device

### 2. Saving 2 runners in same folder
 - for this modified the commands such that each runner will extract into a specific folder rather than default code
 - modified commands :

    ```shell
    # download the runner zip
   curl https://product-downloads.atlassian.com/software/bitbucket/pipelines/atlassian-bitbucket-pipelines-runner-2.1.0.tar.gz --output runner-1-atlassian-bitbucket-pipelines-runner.tar.gz

   # extract the file
   mkdir runner-1-atlassian-bitbucket-pipelines-runner && tar -xzvf runner-1-atlassian-bitbucket-pipelines-runner.tar.gz -C runner-1-atlassian-bitbucket-pipelines-runner

   # launch the runner
   cd runner-1-atlassian-bitbucket-pipelines-runner/bin

   nohup ./start.sh --accountUuid {**********} --repositoryUuid {**********} --runnerUuid {**********} --OAuthClientId ********** --OAuthClientSecret ********** --runtime linux-shell --workingDirectory ../temp > runner-1.log 2>&1 &
    ```

 - and similarly for runner 2 as well
 - on starting both runners in linux host, they shown online in bitbucket

### Runners Same Folder Setup

```shell
├── runners
│   │
│   ├── runner-1-atlassian-bitbucket-pipelines-runner
│   │   └── bin
│   │       ├── runner-1.log
│   │       └── start.sh
│   │
│   ├── runner-1-atlassian-bitbucket-pipelines-runner.tar.gz
│   │
│   ├── runner-2-atlassian-bitbucket-pipelines-runner
│   │   └── bin
│   │       ├── runner-2.log
│   │       └── start.sh
│   │
│   └── runner-2-atlassian-bitbucket-pipelines-runner.tar.gz
│
└── starter.sh
```

> NOTE - `starter.sh` is a shell script made to start both runners, store logs of each run and print the PS of each runner process 

### Runners Created and Online

![alt text](<./images/Screenshot from 2024-06-20 11-56-56.png>)


### 3. Creating Project and Repository
 - Go to Bitbucket Home Page -> Create -> **Project** & Fill necessary details
 - Then go to Bitbucket Home Page -> Create -> **Repository**
 - In project select previously made project and fill necessary details

### 4. Bitbucket Pipeline
 - First Iteration of code had 2 separate runners and each uploaded file with different name onto a AWS S3 Bucket 
 - Second Iteration of code had triggers (main, hotflix/**, pull requests, tags)
 - Third Iteration of code uses variables to give name to the file to be uploaded

### 5. Run Pipeline 

![alt text](<./images/Screenshot from 2024-06-20 11-02-54.png>)

Files uploaded on S3 Bucket 

![alt text](<./images/Screenshot from 2024-06-20 11-22-39.png>)




