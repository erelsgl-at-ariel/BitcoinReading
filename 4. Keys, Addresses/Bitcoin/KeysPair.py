from ecpy.curves import Curve, Point

P = 1000  # modulo 17
publicKey = (12, 16)    # example for public key modulo 17

c = Curve.get_curve('secp256k1')    # using the "y^3 = x^2 +7" curve for generate key
p = Point(0x65d5b8bf9ab1801c9f168d4815994ad35f1dcb6ae6c7a1a303966b677b813b00,
          0xe6b865e529b8ecbf71cf966e900477d49ced5846d7662dd2dd11ccd55c0aff7f, c)    # point p is on the curve

privateKey = 0  # initial as null
for i in range(100000):     # limit the search to 100000. means give up.
    currentPoint = i*p      # generate some public key - need to check if this is the our public key
    if (currentPoint.x % P) == publicKey[0] and (currentPoint.y % P) == publicKey[1]:
        privateKey = i      # private key found!
        break


if(privateKey):
    print("Private Key is: ", privateKey)
else:       # no private key found
    print("Private Key not found!!")

