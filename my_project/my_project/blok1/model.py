"""demo Example model, this model is goging to create table at startup
"""
from anyblok import Declarations
from anyblok.column import Integer, String


Model = Declarations.Model


@Declarations.register(Model)
class Example():
    """ Example Model, see more column field
    http://anyblok.readthedocs.io/en/latest/MEMENTO.html#column
    """
    id = Integer(primary_key=True)
    name = String(label="Name", unique=True, nullable=False)

    def __str__(self):
        return ('{self.name}').format(self=self)

    def __repr__(self):
        msg = ('<Example: {self.name}, {self.id}>')
        return msg.format(self=self)
