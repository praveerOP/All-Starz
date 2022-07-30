import React from "react";
import Toolbar from "@material-ui/core/Toolbar";
import AppBar from "@material-ui/core/AppBar";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import Button from "@material-ui/core/Button";
import MenuIcon from "@material-ui/icons/Menu";

function Navbar() {

  return (
    // <div classname = "navbar">
    <>
        <AppBar style={{ background: '#2E3B55' }}>
        <Toolbar>
          <IconButton
            edge="start"
            style={{
              marginRight: 20,
            }}
            color="inherit"
            aria-label="menu"
          >
            <MenuIcon />
          </IconButton>
          <Typography
            variant="h6"
            style={{
              flexGrow: 1,
              color: "#d0ab00",
            }}
          >
            All Starz
          </Typography>
          <Button color="inherit">Trends</Button>
          <Button color="inherit">Products</Button>
          {/* <Button color="inherit">Trends</Button> */}
        </Toolbar>
      </AppBar>
      <Toolbar />
      </>
  )
}

export default Navbar;