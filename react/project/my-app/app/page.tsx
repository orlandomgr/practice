'use client'
import * as React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import Divider from '@mui/material/Divider';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';
import EditIcon from '@mui/icons-material/Edit';

import { useState } from 'react';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import Paper from '@mui/material/Paper';
import IconButton from '@mui/material/IconButton';
import { Button } from '@mui/material';

import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import { styled } from '@mui/material/styles';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import NativeSelect from '@mui/material/NativeSelect';
import InputBase from '@mui/material/InputBase';
import { Theme, useTheme } from '@mui/material/styles';
import OutlinedInput from '@mui/material/OutlinedInput';


// function JiraItem( {jira, onJiraClick }){
//   return (
//     <div className="card" onClick={onJiraClick}>
//       <img src="jira_logo.png" alt="Avatar"/>
//       <h4><b>{jira.id}</b></h4>
//       <p>{jira.title}</p>
//     </div>    
//   )
// }

function Board({ jiraArray }) {
  function onCreateJiraClick() {
    setJiraTitle("")
    setJiraDescription("")
    setJiraStatus("open")
    setMainId(mainId + 1);
    setJiraId(mainId)
    setOpen(true)
  }
  function handleClose() {
    setOpen(false)
  }

  function handleSave() {
    let jiraItem = {
      id: "" + jiraId,
      title: jiraTitle,
      description: jiraDescription,
      status: jiraStatus
    }

    let exist = false
    let i = 0
    for (let jira of jiraArray) {
      if (jira && jira.id == jiraId) {
        exist = true
        break
      }
      i += 1
    }
    if (exist) {
      delete jiraArray[i]
    }
    jiraArray.push(jiraItem)

    setOpen(false)
    refreshLists()
  }


  let openItems = jiraArray.filter(jira => jira.status == "open")
  let progressItems = jiraArray.filter(jira => jira.status == "progress")
  let doneItems = jiraArray.filter(jira => jira.status == "done")

  function refreshLists() {
    openItems = jiraArray.filter(jira => jira.status == "open")
    progressItems = jiraArray.filter(jira => jira.status == "progress")
    doneItems = jiraArray.filter(jira => jira.status == "done")
  }

  const [open, setOpen] = React.useState(false);
  const [mainId, setMainId] = React.useState(1);
  const [jiraId, setJiraId] = React.useState(1);

  // let jiraTitle = "";
  // let jiraDescription = "";
  // let jiraStatus = "open";

  const [jiraTitle, setJiraTitle] = React.useState("");
  const [jiraDescription, setJiraDescription] = React.useState("");
  const [jiraStatus, setJiraStatus] = React.useState("open");

  function updateTitle(event: React.ChangeEvent<HTMLInputElement>) {
    setJiraTitle(event.target.value as string);
  };

  function updateDescription(event: React.ChangeEvent<HTMLInputElement>) {
    setJiraDescription(event.target.value as string);
  };

  function updateStatus(event: SelectChangeEvent) {
    setJiraStatus(event.target.value as string)
  }

  function editJira(event) {
    let eventId = parseInt(event.target.parentElement.id)

    for (let jira of jiraArray) {
      if (jira && jira.id == eventId) {
        setJiraId(jira.id)
        setJiraTitle(jira.title)
        setJiraDescription(jira.description)
        setJiraStatus(jira.status)
        setOpen(true)
      }
    }

  }

  return (
    <>
      <button className="square" onClick={onCreateJiraClick}>
        Create Jira
      </button>
      <br />

      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>New/Edit Jira</DialogTitle>
        <DialogContent>
          {/* <DialogContentText>
          </DialogContentText> */}
          <form onSubmit={handleSave} id="subscription-form">
            <TextField
              autoFocus
              required
              margin="dense"
              id="jiraId"
              name="jiraId"
              label="Jira ID"
              type="number"
              value={jiraId}
              slotProps={{
                htmlInput: { readOnly: true }
              }}
              fullWidth
              variant="standard"
            />
            <TextField
              autoFocus
              required
              margin="dense"
              id="jiraTitle"
              name="jiraTitle"
              label="Title"
              type="text"
              value={jiraTitle}
              onChange={updateTitle}
              fullWidth
              variant="standard"
            />
            <TextField
              autoFocus
              required
              margin="dense"
              id="jiraDescription"
              name="jiraDescription"
              label="Description"
              type="text"
              value={jiraDescription}
              onChange={updateDescription}
              fullWidth
              variant="standard"
            />
            <FormControl sx={{ m: 1, width: 300 }}>
              <InputLabel id="jiraStatus">Status</InputLabel>
              <Select
                labelId="jiraStatus"
                id="jiraStatus"
                value={jiraStatus}
                onChange={updateStatus}
                input={<OutlinedInput label="Status" />}
              >
                <MenuItem value={"open"}>Open</MenuItem>
                <MenuItem value={"progress"}>In Progress</MenuItem>
                <MenuItem value={"done"}>Done</MenuItem>
              </Select>
            </FormControl>

          </form>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleSave} type="submit" form="subscription-form">
            Save
          </Button>
        </DialogActions>
      </Dialog>

      <div className='jiraBoard'>
        <div className='jiraColumn'>
          <h2>
            Open
          </h2>
          <List sx={{ width: '30%', maxWidth: 360, bgcolor: 'background.paper' }}>
            {openItems.map((jira) => (
              <div key={jira.id}>
                <ListItem alignItems="flex-start">
                  <ListItemText
                    key={jira.id}
                    id={jira.id}
                    primary={jira.id}
                    secondary={jira.title}
                    onClick={editJira}
                  />
                </ListItem>
                <Divider className="jiraDivider" variant="inset" component="li" />
              </div>
            ))}
          </List>
        </div>
        <div className='jiraColumn'>
          <h2>
            In progress
          </h2>
          <List sx={{ width: '30%', maxWidth: 360, bgcolor: 'background.paper' }}>
            {progressItems.map((jira) => (
              <div key={jira.id}>
                <ListItem alignItems="flex-start">
                  <ListItemText
                    key={jira.id}
                    id={jira.id}
                    primary={jira.id}
                    secondary={jira.title}
                    onClick={editJira}
                  />
                </ListItem>
                <Divider className="jiraDivider" variant="inset" component="li" />
              </div>
            ))}
          </List>
        </div>
        <div className='jiraColumn'>
          <h2>
            Done
          </h2>
          <List sx={{ width: '30%', maxWidth: 360, bgcolor: 'background.paper' }}>
            {doneItems.map((jira) => (
              <div key={jira.id}>
                <ListItem alignItems="flex-start">
                  <ListItemText
                    key={jira.id}
                    id={jira.id}
                    primary={jira.id}
                    secondary={jira.title}
                    onClick={editJira}
                  />
                </ListItem>
                <Divider className="jiraDivider" variant="inset" component="li" />
              </div>
            ))}
          </List>
        </div>
      </div>
    </>
  );
}

export default function Game() {

  async function getData() {
    const url = "https://api.restful-api.dev/objects";
    try {
      const response1 = await fetch(url);
      if (!response1.ok) {
        throw new Error(`Response status: ${response1.status}`);
      }

      const response2 = response1.clone();

      const result1 = await response1.json();
      const result2 = await response2.json();
      return result1
    } catch (error) {
      console.error(error.message);
    }
  }

  async function addData(data) {
    const url = "https://api.restful-api.dev/objects";
    try {
      const response1 = await fetch(
        url,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data)
        }
      );
      if (!response1.ok) {
        throw new Error(`Response status: ${response1.status}`);
      }

      const result1 = await response1.json();
      return result1
    } catch (error) {
      console.error(error.message);
    }
  }

  const [jiraArray] = useState([{}]);
  // const [currentMove, setCurrentMove] = useState(0);
  // const xIsNext = currentMove % 2 === 0;
  // const currentSquares = history[currentMove];


  // jiraArray.push(jiraItem)
  async function onClickGet() {
    let data = await getData()
    console.log(data)

  }

  async function onClickPost() {
    let data = {
      "name": "Apple MacBook Pro 2026",
      "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
      }
    }
    let result = await addData(data)
    console.log(result)

  }

  return (
    <div className="game">
      <button className="square" onClick={onClickGet}>
        Test Get
      </button>
      <button className="square" onClick={onClickPost}>
        Test Post
      </button>

      <div className="game-board">
        <Board jiraArray={jiraArray} />
      </div>
    </div>
  );
}
