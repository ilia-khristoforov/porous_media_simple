import gmsh

def create_hexahedral_mesh(step_file, output_mesh_file, characteristic_length):
    # Initialize Gmsh
    gmsh.initialize()

    # Load the STEP model
    gmsh.merge(step_file)

    # Set the characteristic length for mesh elements
    gmsh.model.mesh.setSize(gmsh.model.getEntities(0), characteristic_length)
    gmsh.option.setNumber("Mesh.Algorithm", 8)  # 8 corresponds to hexahedral elements


    # Create a hexahedral mesh
    gmsh.model.mesh.generate(3)

    # Save the mesh to a temporary file in binary format
    
    temp_mesh_file = "temp_mesh.unv"
    gmsh.write(temp_mesh_file)


    # Finalize Gmsh
    gmsh.finalize()

if __name__ == "__main__":
    # Specify the input STEP file, output mesh file, and characteristic length
    step_file = "fluid.STEP"
    output_mesh_file = "GFG.unv"
    characteristic_length = 2  # Adjust this value based on your requirements

    # Create the hexahedral mesh
    create_hexahedral_mesh(step_file, output_mesh_file, characteristic_length)