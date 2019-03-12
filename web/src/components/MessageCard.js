import React from "react";
import Card from "@material-ui/core/Card";
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';


const MessageCard = ({ from_id='me', date,  text }) => {
  return (
    <Card>
      <CardContent>
        <Typography variant="h5" component="h2">
          [{from_id}]: { text }
        </Typography>
        <Typography color="textSecondary">
          { date }
        </Typography>
      </CardContent>
    </Card>
  );
}

export default MessageCard;