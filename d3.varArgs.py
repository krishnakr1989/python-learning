def deploy(application, *args, **kwargs):
    print(application)
    print(args)
    print(kwargs)
    print(type(args))
    print(type(kwargs))

deploy(
    "payment",
    "prod",
    "blue-green",
    name="payment-service",
    replicas=5,
    image="payment:2.1"
)