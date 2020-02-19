import tensorflow as tf
import tensorflow_hub as hub
def embed_useT(module):
    with tf.Graph().as_default():
        sentences = tf.placeholder(tf.string)
        embed = hub.Module(module)
        embeddings = embed(sentences)
        session = tf.train.MonitoredSession()
    return lambda x: session.run(embeddings, {sentences: x})
embed_fn = embed_useT('/home/gourav/Desktop/aries/testbot/model/3(1)')    
x="this is first question"
y="this is first question"
messages = [x,y]
embed_fn(messages)
encoding_matrix = embed_fn(messages)
import numpy as np
arr=np.inner(encoding_matrix, encoding_matrix)
arr
