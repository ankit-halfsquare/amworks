var menu_data = [
  {
    id: "dashboard",
    icon: "mdi mdi-view-dashboard",
    value: "Add Building",
    data: [
      // { id: "dashboard1", value: "&nbsp&nbsp&nbspItems"},
      // { id: "dashboard2", value: "&nbsp&nbsp&nbspView-Access Level-User"}
    ],
  },
  // {id: "layouts", icon: "mdi mdi-view-column", value:"Projects (Task Sets)", data:[
  // 	{ id: "accordions", value: "Tasks"},
  // 	{ id: "portlets", value: "&nbsp&nbsp&nbspView-Role-Position-User"},
  // 	{ id: "portlets1", value: "&nbsp&nbsp&nbspView-Role-User"},
  // 	{ id: "portlets2", value: "&nbsp&nbsp&nbspProject-Position"}
  // ]},
  // {id: "tables", icon: "mdi mdi-table", value:"Building Project Summary", data:[
  // 	{ id: "tables1", value: "Datatable"},
  // 	{ id: "tables2", value: "TreeTable"},
  // 	{ id: "tables3", value: "Pivot"}
  // ]},
  // {id: "blank", icon: "", value:""},
  // {id: "uis", icon: "mdi mdi-puzzle", value:"UI Components", data:[
  // 	{ id: "dataview", value: "DataView"},
  // 	{ id: "list", value: "List"},
  // 	{ id: "menu", value: "Menu"},
  // 	{ id: "tree", value: "Tree"}
  // ]},
  // {id: "po", icon: "mdi mdi-calendar", value:"<i>Platform Owners</i>"},
  // {id: "po1", icon: "mdi mdi-calendar", value:"Users"},
  // {id: "po2", icon: "mdi mdi-calendar", value:"Platform Owners"},
  // {id: "po3", icon: "mdi mdi-calendar", value:"People"},
  // {id: "demo", icon: "mdi mdi-book", value:"Dashboard"}
];

var menu_data2 = [
  {
    id: "dashboard",
    icon: "mdi mdi-view-dashboard",
    value: "View Records",
    // data: [
    //   { id: "dashboard1", value: "&nbsp&nbsp&nbspItems" },
    //   { id: "dashboard2", value: "&nbsp&nbsp&nbspView-Access Level-User" },
    // ],
  },
  {
    id: "layouts",
    icon: "mdi mdi-view-column",
    value: "Projects (Task Sets)",
    data: [
      { id: "accordions", value: "Tasks" },
      { id: "portlets", value: "&nbsp&nbsp&nbspView-Role-Position-User" },
      { id: "portlets1", value: "&nbsp&nbsp&nbspView-Role-User" },
      { id: "portlets2", value: "&nbsp&nbsp&nbspProject-Position" },
    ],
  },
  {
    id: "tables",
    icon: "mdi mdi-table",
    value: "Building Project Summary",
    data: [
      { id: "tables1", value: "Datatable" },
      { id: "tables2", value: "TreeTable" },
      { id: "tables3", value: "Pivot" },
    ],
  },
  { id: "blank", icon: "", value: "" },
  // {id: "uis", icon: "mdi mdi-puzzle", value:"UI Components", data:[
  // 	{ id: "dataview", value: "DataView"},
  // 	{ id: "list", value: "List"},
  // 	{ id: "menu", value: "Menu"},
  // 	{ id: "tree", value: "Tree"}
  // ]},
  { id: "po", icon: "mdi mdi-calendar", value: "<i>Platform Owners</i>" },
  { id: "po1", icon: "mdi mdi-calendar", value: "Users" },
  { id: "po2", icon: "mdi mdi-calendar", value: "Platform Owners" },
  { id: "po3", icon: "mdi mdi-calendar", value: "People" },
  { id: "demo", icon: "mdi mdi-book", value: "Dashboard" },
];

const fetchApi = async () => {
  const response = await fetch(
    "https://amworksweb.azurewebsites.net/core/api/test-building/",
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  var data = await response.json();
  res = data;

  res.forEach((row) => {
    if (row.status == "o") {
      row.status = "Open";
    } else if (row.status == "c") {
      row.status = "Closed";
    } else if (row.status == "l") {
      row.status = "Lost";
    }
  });
  return res;
};
