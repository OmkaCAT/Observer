from Publisher import Publisher
from Subscriber import Subscriber

pub = Publisher()

sub1 = Subscriber('Sub1')
sub2 = Subscriber('Sub2')
sub3 = Subscriber('Sub3')

pub.register(sub1)
pub.register(sub2)
pub.register(sub3)

pub.dispath("Message!")
