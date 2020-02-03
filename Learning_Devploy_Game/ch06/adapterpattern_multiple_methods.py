"""
    作者:北辰
    日期:28/05/2019
    功能:兽人之袭游戏设计模式之适配器模式:使用python方法实现多适配器方法
"""

class FooElf:
    """ An imaginary third-party class that has an incompatible interface.

    FooElf represents a game character class that is provided by an imaginary
    'third party' developer. It does not have the 'jump' and 'attack' methods
    that the client code expects (incompatible interface).

    This is used to illustrate one way of implementing the adapter pattern
    when you have multiple methods that have incompatible names

   .. seealso:: `ForeignUnitAdapter`
   """
    def leap(self):
        """leap method is equivalent to the 'jump' method client expects

        The adapter should have a jump method which in turn calls this.
        """
        print("FooElf.leap")
    def hit(self):
        """hit method is equivalent to the 'attack' method client expects

        The adapter should have an attack method which in turn calls this.
        """
        print("FooElf.hit")

class ForeignUnitAdapter:
    """Generalized adapter class for 'fixing' incompatible interfaces.

   :arg adaptee: An instance of the 'adaptee' class. For example, FooElf
             is an adaptee as it has a method 'leap' when we expect 'jump'
   """
    def __init__(self,adaptee):
        self.foreign_unit = adaptee

    def __getattr__(self,item):
        """Handle all the undefined attributes the client code expects.

        :param item: name of the attribute.
        :return: Returns the corresponding attribute of the adaptee instance
        (self.foreign_unit)
        .. todo:: Add exception handling code.
        """
        return getattr(self.foreign_unit,item)

    def set_adapter(self,name,adaptee_method):
        """Convenience method to set a new attribute to this class
        :arg name: Name of the new attribute.
        :arg adaptee_method: The 'value' of the new attribute.
             The adaptee_method will be assigned as a value.
        Example: setattr(self, 'jump', foo_elf.leap) is equivalent to saying:
        self.jump = foo_elf.leap
        """
        setattr(self,name,adaptee_method)

if __name__ == '__main__':
    foo_elf = FooElf()
    foo_elf_adapter = ForeignUnitAdapter(foo_elf)

    foo_elf_adapter.set_adapter("jump",foo_elf.leap)
    foo_elf_adapter.set_adapter("attack",foo_elf.hit)

    # Optionally, assign the adapter methods directly:
    # foo_elf_adapter.jump = foo_elf.leap
    # foo_elf_adapter.attack = foo_elf.hit

    foo_elf_adapter.jump()
    foo_elf_adapter.attack()

