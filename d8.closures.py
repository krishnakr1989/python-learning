def create_deployer(environment):

    def deploy(application):
        
        print(
            f"Deploying {application} "
            f"to {environment}"
        )
    return deploy

prod_deploy = create_deployer("prod")
dev_deploy = create_deployer("dev")

prod_deploy("payment")
dev_deploy("payment")