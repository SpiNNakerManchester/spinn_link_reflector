import spynnaker8 as p

p.setup(1.0, n_chips_required=2)
print "starting work"
# shouldnt need this, but we do. oops.
p.Population(1, p.IF_curr_exp, {}, label="Stupid requirement ;-)")
# note that in Pynn0.9 we don't have a run forever yet
p.run(2 ^ 31)
print "woop!"
p.end()
