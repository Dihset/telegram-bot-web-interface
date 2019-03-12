import React from "react";
import { Link } from 'react-router-dom';
import Card from "@material-ui/core/Card";
import CardActionArea from '@material-ui/core/CardActionArea';

const styleDialogCard = {
  margin: "10px",
  paddingLeft: "20px",
  paddingRight: "20px"
};

const styleLink = {
  textDecoration: "none",
  color: 'black'
}; 

const DialogCard = ({ pk, username='', first_name='', last_name='', history}) => {
  
  return (
    <Card style={styleDialogCard}>
      <Link
        to={{ pathname: 'dialog/' + pk }}
        style={styleLink}
      >
        <CardActionArea>
          <h5>{ username }</h5>
          <p>{ first_name + ' ' + last_name }</p>
        </CardActionArea>
      </Link>
    </Card>
  );
}
export default DialogCard;
