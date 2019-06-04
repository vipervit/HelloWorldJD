pipeline {

  agent any
    stages {
      stage('Deploy') {
        steps('Make and push docker image') {
          sh 'docker build -t tesqos/demojd .'
          sh 'docker push tesqos/demojd'
        }
      }
    }
}
