pipeline {
    agent any
    stages {
        stage('Welcome Step') {
            steps { 
                echo 'Welcome to the LambdaTest'
            }
        }
        stage('check if py file exists') {
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
                script {
                    def lastSuccessBuildName = Jenkins.instance.getItemByFullName('multiP/branch2').lastSuccessfulBuild.displayName
                    echo "Last Success Build Name: ${lastSuccessBuildName}"
                    
                    echo "Description: ${lastSuccessBuildName.getUpUrl()}"
                    echo "${env.JOB_NAME}"
                }
            }
        }
    }
}
