import requests
import hashlib
import os



HASH_1 = '098f6bcd4621d373cade4e832627b4f6'   # 'test'
HASH_2 = '5eb63bbbe01eeed093cb22bb8f5acdc3'   # 'hello world'
FIB_SEQ = [0,1,1,2,3,5,8,13,21,34]
HTTP_ENCODE = "This%20is%20a%20longer%20string.%0D%0AIt%20even%20includes%20a%20newline..."

print ("Testing API for expected results...\n")

tests = {
    '/md5/test':                    (200, HASH_1),
    '/md5/hello%20world':           (200, HASH_2),
    '/md5':                         (404, None),
    '/factorial/4':                 (200, 24),
    '/factorial/5':                 (200, 120),
    '/factorial/test':              (404, None),
    '/factorial/0':                 (200, 1),
    '/fibonacci/8':                 (200, FIB_SEQ[:7]),
    '/fibonacci/35':                (200, FIB_SEQ),
    '/fibonacci/test':              (404, None),
    '/fibonacci/1':                 (200, FIB_SEQ[:3]),
    '/is-prime/1':                  (200, False),
    '/is-prime/2':                  (200, True),
    '/is-prime/5':                  (200, True),
    '/is-prime/6':                  (200, False),
    '/is-prime/37':                 (200, True),
    '/slack-alert/test':            (200, True),
    '/slack-alert/'+HTTP_ENCODE:    (200, True),
	'/kv-record/testval':			(200, True),   #records testval like normal
	'/kv-record/testval':			(404, False),  #can't record becuase value exists already
	'/kv-retrieve/testval':			(200, True),   #retrieves testval like normal
	'/kv-retrieve/badval':			(404, False),  #can't retrieve badval, doesnt exist
}

FAILED = 0
PASSED = 0
for uri, test_result in tests.items():
    print " * ", uri, "... ",
    resp = requests.get('http://localhost:5000'+uri)
    if resp.status_code == test_result[0]:
        try:
            # Try and extract the JSON from the HTTP results
            output = resp.json()['output']
        except:
            # An exception means there was no JSON returned from the API (error)
            output = "Cannot read JSON payload (failed to locate  'output' key)!"

        # Check the tests array for the expected results
        if test_result[1] == None or output == test_result[1]:
            print "Passed"
            PASSED += 1
        else:
            print "FAILED"
            print "          - Expected output: '%s'" % str(test_result[1])
            print "          - Actual output:   '%s'" % str(output)
            FAILED += 1
    else:
        print "FAILED"
        print "          - Expected HTTP status: %i" % test_result[0]
        print "          - Actual HTTP status:   %i" % resp.status_code
        FAILED += 1

rate = float(PASSED) / float(FAILED+PASSED) * 100.0
print "\n\n Passed %i of %i tests (%i%% Success rate)" % (PASSED, FAILED+PASSED, rate)