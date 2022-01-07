rpipeline {
    agent any
    stages {
        stage('Welcome Step') {
            steps { 
                echo 'Welcome to the LambdaTest'
            }
        }
        stage('check if py file exists'){
            steps {
                
                script {
                    if(fileExists("./branch2_1/pyTest1.py")) {
                        echo 'py file exists'
                    }
                    else {
                        echo '404: file not exists'
                    }
                }
                
            }
            
        }
        stage('test new') {
            steps {
                script{
                    
                    def bb = Jenkins.instance.getItemByFullName('multiP/branch2')
                    echo "Last Success Build Name: ${bb.getLastSuccessfulBuild()}"
                    echo "Description: ${bb.getFullDisplayName()}"
                    echo "${env.JOB_NAME}"
                }
            }
        }
    }
}
