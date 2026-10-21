def process(**kk):
    for k,v in kk.items():
        print( f"key {k}, value {v}")

process(name="payment-service", replicas=5, image="payment:2.1")