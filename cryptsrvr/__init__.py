# 3rd party libs
import flask

# custom lib
import crypt

# create Flask instance
app = flask.Flask(__name__)

# get sha256 hash of NONCE environment variable and add to app config dic
app.config['NONCE_HASH'] = crypt.get_nonce_hash()

# define route decorators
@app.route('/')
def server_up_greeting():
    return 'Flask Server Up!'

@app.route('/test/purchases')
def test_purchases():
    return flask.render_template()

@app.route('/test/download/<pop>/<poe>/<file_name>')
def test_dwnldr(pop, poe, file_name):
    # get new pointer to NONCE in app.config
    nonce_hash = app.config['NONCE_HASH']

    # get duplicate proof of purchase (PoP) for comparing with client PoP
    dup_pop = crypt.sha256(file_name + nonce_hash)

    # check PoP submitted by client (similiar to BTC Proof of Work)
    if pop != dup_pop:
        # return standard 404 status code for curious hackers
        flask.abort(404)

    # generate Proof of Expiration (PoE) hash by scrambling PoP hash
    poe_nonce = crypt.scramble_hash(dup_pop)

    # encode with current datetime
    dup_poe = crypt.encode_dtime(poe_nonce)

    # check PoE submitted by client (similar to Proof of Purchase above)
    if poe <= dup_poe:
        # access has expired
        flask.abort(403)

    # if the client gets this far they deserve a prize
    return flask.send_from_directory('media',
                                     file_name,
                                     mimetype='audio/mpeg',
                                     as_attachment=True)
