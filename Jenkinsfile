pipeline {
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
                    /*
                    def lastSuccessBuildName = Jenkins.instance.getItem(env.JOB_NAME).lastSuccessfulBuild.displayName
                    echo "Last Success Build Name: ${lastSuccessBuildName}"
                    */
                    echo "${env.JOB_NAME}"
                }
            }
        }
    }
}
