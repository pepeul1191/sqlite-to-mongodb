### Migraciones

Migraciones con DBMATE:

    $ dbmate -d "migrations" -e "DB" new <<nombre_de_migracion>>
    $ dbmate -d "migrations" -e "DB" up
    $ dbmate -d "migrations" -e "DB" rollback


### Consultas MongoDB

``` javascript
// proyección
db.getCollection("pokemon_types").find({},{name: 1, _id: 0})
// seleccionar todos
db.getCollection("pokemon_types").find()
// quitar campo
db.nombre_coleccion.updateMany({}, { $unset: { nombre_campo: "" } })
// insertar varios
db.pokemon_types.insertMany([
	{"id": 1, "name": "PLANTA"},
	{"id": 2, "name": "VENENO"},...
])
// contar
db.locations.find({'type': 'department'}).count()
// borrar colección
db.pokemon_types.drop()
// borrar documentos - todos
db.locations.deleteMany({})
// find in array
db.pokemon_types.find({ id: { $in: ['1', '2'] } })
// joins?
db.pokemons.aggregate([
  {
    $lookup: {
      from: "generations",
      localField: "generation_id",
      foreignField: "_id",
      as: "generation"
    }
  },
  {
    $project: {
      "id: 0,
      "generation_id": 0
    }
  },
  {
    $addFields: {
      generation: { $arrayElemAt: ["$generation", 0] }
    }
  },
  {
    $unwind: "$pokemon_types"
  },
  {
    $lookup: {
      from: "pokemon_types",
      localField: "pokemon_types",
      foreignField: "_id",
      as: "pokemon_types"
    }
  },
  {
    $addFields: {
      pokemon_types: { $arrayElemAt: ["$pokemon_types", 0] }
    }
  },

])


```

