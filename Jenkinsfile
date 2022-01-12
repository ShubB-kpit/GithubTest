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
                    
                    //echo "Description: ${lastSuccessBuildName.getUpUrl()}"
                    //echo "${env.JOB_NAME}"
                    
                    echo "BUILD_NUMBER :: ${BUILD_NUMBER}"
                    echo "BUILD_ID :: ${BUILD_ID}"
                    echo "BUILD_DISPLAY_NAME :: ${BUILD_DISPLAY_NAME}"
                    echo "JOB_NAME :: ${JOB_NAME}"
                    echo "JOB_BASE_NAME :: ${JOB_BASE_NAME}"
                    echo "BUILD_TAG :: ${BUILD_TAG}"
                    echo "EXECUTOR_NUMBER :: ${EXECUTOR_NUMBER}"
                    echo "NODE_NAME :: ${NODE_NAME}"
                    echo "NODE_LABELS :: ${NODE_LABELS}"
                    echo "WORKSPACE :: ${WORKSPACE}"
                    echo "JENKINS_HOME :: ${JENKINS_HOME}"
                    echo "JENKINS_URL :: ${JENKINS_URL}"
                    echo "BUILD_URL ::${BUILD_URL}"
                    echo "JOB_URL :: ${JOB_URL}"
                    
                }
            }
        }
    }
}
