def configure(ctx):
        pass

from waflib.Task import Task
class cp(Task): 1
        def run(self): 2
                return self.exec_command('cp %s %s' % (
                                self.inputs[0].abspath(), 3
                                self.outputs[0].abspath()
                        )
                )

class cat(Task):
        def run(self):
                return self.exec_command('cat %s %s > %s' % (
                                self.inputs[0].abspath(),
                                self.inputs[1].abspath(),
                                self.outputs[0].abspath()
                        )
                )

def build(ctx):

        cp_1 = cp(env=ctx.env) 4
        cp_1.set_inputs(ctx.path.find_resource('wscript')) 5
        cp_1.set_outputs(ctx.path.find_or_declare('foo.txt'))
        ctx.add_to_group(cp_1) 6

        cp_2 = cp(env=ctx.env)
        cp_2.set_inputs(ctx.path.find_resource('wscript'))
        cp_2.set_outputs(ctx.path.find_or_declare('bar.txt'))
        ctx.add_to_group(cp_2)

        cat_1 = cat(env=ctx.env)
        cat_1.set_inputs(cp_1.outputs + cp_2.outputs)
        cat_1.set_outputs(ctx.path.find_or_declare('foobar.txt'))
        ctx.add_to_group(cat_1)
