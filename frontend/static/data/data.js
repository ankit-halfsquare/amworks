var menu_data = [
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

var dataset1 = [
  {
    id: 7,
    organization_id: 40,
    name: "Ankit new",
    code: "Repellendus Nostrud aut dolorum repellendus Culp",
    city: "Porro laborum Quasi praesentium doloremque in dol",
    state: "Cum nostrud ullam doloremque nisi culpa cupidatat",
    country: "Dolore dolor ab sequi nulla omnis odio obcaecati e",
    status: "Consequatur A explicabo Magna ut duis sint accus",
    create_date: "2022-08-30T05:20:29Z",
    create_user: 56,
    update_date: "2022-08-30T05:20:31Z",
    update_user: 65,
    obsolete: 96,
    comments: "In iure et quibusdam",
    ta1_alias:
      "Ullam laboris elit sunt unde aliqua Adipisicing quis aspernatur at placeat voluptate",
    ta2_alias: "Ut accusamus non atque magni atque",
    ta3_alias:
      "Enim distinctio Id similique eu nihil sit architecto quo nesciunt qui quis cum aut et quibusdam molestiae",
    ta4_alias: "Vitae nostrud sit eos aut",
    ta5_alias:
      "Fuga Dolorum non dolor a consequuntur quia repudiandae velit reiciendis consectetur quidem duis vitae iure possimus magnam aut itaque cum",
    ta6_alias:
      "Sit voluptate laboris est mollit quos dolore quo aliquam consectetur molestias",
    ta7_alias:
      "Corrupti sed totam ea optio iusto iste similique Nam rerum veniam deleniti quis sed cillum quasi ducimus praesentium quo",
    ta8_alias:
      "Aut qui qui ipsum alias ipsum sed id quasi sint neque libero incididunt exercitationem consequatur Illo delectus vel iure ut",
    ta9_alias:
      "Accusamus voluptatem voluptas dolor ex ipsa ipsa vel magnam voluptas dolore officia fugit illum odit a fugiat veritatis quaerat",
    ta10_alias: "Amet rerum id non voluptatum ut molestias velit cillum",
    ta11_alias:
      "Corporis voluptatum dolor minima in explicabo Quia doloremque eius lorem est qui tempor saepe voluptatem",
    ta12_alias:
      "Architecto soluta laboriosam sunt distinctio Sit laborum Enim reprehenderit distinctio Anim",
    ta13_alias: "Elit numquam aliquam ut doloremque fugiat suscipit omnis",
    ta14_alias:
      "Ut ut reprehenderit nostrud provident qui consequat Id molestiae ipsum ea obcaecati",
    ta15_alias: "Nisi ea numquam nulla sunt labore ad elit",
    ta16_alias: "Rerum consequuntur sapiente aute aut et et velit iure",
    ta17_alias: "Eius illo fugiat velit sint voluptatem Et quidem",
    ta18_alias: "Error pariatur Dolor aperiam eos placeat consectetur",
    ta19_alias:
      "Est est minim impedit quis quis sit eos corrupti fugiat non aliquid nemo sit molestiae",
    ta20_alias: "Velit autem iusto amet non iste deleniti debitis assumenda",
    sl1_alias:
      "Sit do aut in enim neque commodo dolore culpa qui suscipit eos id",
    sl1_list: 94,
    sl2_alias:
      "Ad fugiat sit non omnis voluptatem voluptatum ullam eligendi aliquid nulla excepteur odit est perspiciatis molestiae in totam nisi",
    sl2_list: 43,
    sl3_alias:
      "Consequatur rerum et velit quia eu rerum velit nihil consectetur et",
    sl3_list: 76,
    sl4_alias:
      "Eligendi voluptate necessitatibus excepteur enim accusamus perferendis ipsum",
    sl4_list: 62,
    sl5_alias: "Et a omnis quidem et",
    sl5_list: 49,
    sl6_alias: "Accusantium sunt dolor lorem fugit dolore",
    sl6_list: 72,
    sl7_alias:
      "Aliquam veritatis maxime provident obcaecati voluptates aut eos sed corrupti doloribus qui amet enim",
    sl7_list: 20,
    sl8_alias: "Veniam recusandae Accusamus quis officia voluptates",
    sl8_list: 95,
    sl9_alias:
      "Anim quia cumque nisi officia nulla in possimus id mollit esse a",
    sl9_list: 21,
    sl10_alias: "Quas dolorem eaque quia aliquip ut eligendi minim",
    sl10_list: 38,
    sl11_alias:
      "Assumenda sed esse et eum odio amet eu velit saepe dignissimos quisquam aperiam reprehenderit doloremque est maiores",
    sl11_list: 2,
    sl12_alias: "Id quia sit deserunt enim fuga Eveniet odio",
    sl12_list: 59,
    sl13_alias: "Adipisci maiores magni duis neque",
    sl13_list: 67,
    sl14_alias:
      "Laboris qui voluptatem et ut qui sunt ratione praesentium ut culpa fuga Doloribus ut",
    sl14_list: 77,
    sl15_alias:
      "Explicabo Veniam voluptate corporis quia architecto iure enim voluptate sint dolore et consequatur ut id",
    sl15_list: 56,
    sl16_alias:
      "Nesciunt maiores sed dolore odit ut quae voluptas cupidatat officiis delectus",
    sl16_list: 40,
    sl17_alias:
      "Sed incidunt necessitatibus recusandae Do delectus dolore earum incidunt voluptas dolore labore dolore quia laboris",
    sl17_list: 95,
    sl18_alias: "Fuga Fugiat adipisci sunt quia dolor nisi",
    sl18_list: 8,
    sl19_alias:
      "Fugit blanditiis officia quia architecto exercitationem rerum quis molestiae elit reprehenderit quas aute dolore",
    sl19_list: 15,
    sl20_alias: "Dolores suscipit itaque neque ex atque amet",
    sl20_list: 76,
    zip: "59257",
    guid: "test",
  },
  {
    id: 8,
    organization_id: 40,
    name: "Ankit",
    code: "Repellendus Nostrud aut dolorum repellendus Culp",
    city: "Porro laborum Quasi praesentium doloremque in dol",
    state: "Cum nostrud ullam doloremque nisi culpa cupidatat",
    country: "Dolore dolor ab sequi nulla omnis odio obcaecati e",
    status: "Consequatur A explicabo Magna ut duis sint accus",
    create_date: "2022-08-30T05:20:29Z",
    create_user: 56,
    update_date: "2022-08-30T05:20:31Z",
    update_user: 65,
    obsolete: 96,
    comments: "In iure et quibusdam",
    ta1_alias:
      "Ullam laboris elit sunt unde aliqua Adipisicing quis aspernatur at placeat voluptate",
    ta2_alias: "Ut accusamus non atque magni atque",
    ta3_alias:
      "Enim distinctio Id similique eu nihil sit architecto quo nesciunt qui quis cum aut et quibusdam molestiae",
    ta4_alias: "Vitae nostrud sit eos aut",
    ta5_alias:
      "Fuga Dolorum non dolor a consequuntur quia repudiandae velit reiciendis consectetur quidem duis vitae iure possimus magnam aut itaque cum",
    ta6_alias:
      "Sit voluptate laboris est mollit quos dolore quo aliquam consectetur molestias",
    ta7_alias:
      "Corrupti sed totam ea optio iusto iste similique Nam rerum veniam deleniti quis sed cillum quasi ducimus praesentium quo",
    ta8_alias:
      "Aut qui qui ipsum alias ipsum sed id quasi sint neque libero incididunt exercitationem consequatur Illo delectus vel iure ut",
    ta9_alias:
      "Accusamus voluptatem voluptas dolor ex ipsa ipsa vel magnam voluptas dolore officia fugit illum odit a fugiat veritatis quaerat",
    ta10_alias: "Amet rerum id non voluptatum ut molestias velit cillum",
    ta11_alias:
      "Corporis voluptatum dolor minima in explicabo Quia doloremque eius lorem est qui tempor saepe voluptatem",
    ta12_alias:
      "Architecto soluta laboriosam sunt distinctio Sit laborum Enim reprehenderit distinctio Anim",
    ta13_alias: "Elit numquam aliquam ut doloremque fugiat suscipit omnis",
    ta14_alias:
      "Ut ut reprehenderit nostrud provident qui consequat Id molestiae ipsum ea obcaecati",
    ta15_alias: "Nisi ea numquam nulla sunt labore ad elit",
    ta16_alias: "Rerum consequuntur sapiente aute aut et et velit iure",
    ta17_alias: "Eius illo fugiat velit sint voluptatem Et quidem",
    ta18_alias: "Error pariatur Dolor aperiam eos placeat consectetur",
    ta19_alias:
      "Est est minim impedit quis quis sit eos corrupti fugiat non aliquid nemo sit molestiae",
    ta20_alias: "Velit autem iusto amet non iste deleniti debitis assumenda",
    sl1_alias:
      "Sit do aut in enim neque commodo dolore culpa qui suscipit eos id",
    sl1_list: 94,
    sl2_alias:
      "Ad fugiat sit non omnis voluptatem voluptatum ullam eligendi aliquid nulla excepteur odit est perspiciatis molestiae in totam nisi",
    sl2_list: 43,
    sl3_alias:
      "Consequatur rerum et velit quia eu rerum velit nihil consectetur et",
    sl3_list: 76,
    sl4_alias:
      "Eligendi voluptate necessitatibus excepteur enim accusamus perferendis ipsum",
    sl4_list: 62,
    sl5_alias: "Et a omnis quidem et",
    sl5_list: 49,
    sl6_alias: "Accusantium sunt dolor lorem fugit dolore",
    sl6_list: 72,
    sl7_alias:
      "Aliquam veritatis maxime provident obcaecati voluptates aut eos sed corrupti doloribus qui amet enim",
    sl7_list: 20,
    sl8_alias: "Veniam recusandae Accusamus quis officia voluptates",
    sl8_list: 95,
    sl9_alias:
      "Anim quia cumque nisi officia nulla in possimus id mollit esse a",
    sl9_list: 21,
    sl10_alias: "Quas dolorem eaque quia aliquip ut eligendi minim",
    sl10_list: 38,
    sl11_alias:
      "Assumenda sed esse et eum odio amet eu velit saepe dignissimos quisquam aperiam reprehenderit doloremque est maiores",
    sl11_list: 2,
    sl12_alias: "Id quia sit deserunt enim fuga Eveniet odio",
    sl12_list: 59,
    sl13_alias: "Adipisci maiores magni duis neque",
    sl13_list: 67,
    sl14_alias:
      "Laboris qui voluptatem et ut qui sunt ratione praesentium ut culpa fuga Doloribus ut",
    sl14_list: 77,
    sl15_alias:
      "Explicabo Veniam voluptate corporis quia architecto iure enim voluptate sint dolore et consequatur ut id",
    sl15_list: 56,
    sl16_alias:
      "Nesciunt maiores sed dolore odit ut quae voluptas cupidatat officiis delectus",
    sl16_list: 40,
    sl17_alias:
      "Sed incidunt necessitatibus recusandae Do delectus dolore earum incidunt voluptas dolore labore dolore quia laboris",
    sl17_list: 95,
    sl18_alias: "Fuga Fugiat adipisci sunt quia dolor nisi",
    sl18_list: 8,
    sl19_alias:
      "Fugit blanditiis officia quia architecto exercitationem rerum quis molestiae elit reprehenderit quas aute dolore",
    sl19_list: 15,
    sl20_alias: "Dolores suscipit itaque neque ex atque amet",
    sl20_list: 76,
    zip: "59257",
    guid: "test",
  },
  {
    id: 9,
    organization_id: 40,
    name: "Ankit",
    code: "Repellendus Nostrud aut dolorum repellendus Culp",
    city: "Porro laborum Quasi praesentium doloremque in dol",
    state: "Cum nostrud ullam doloremque nisi culpa cupidatat",
    country: "Dolore dolor ab sequi nulla omnis odio obcaecati e",
    status: "Consequatur A explicabo Magna ut duis sint accus",
    create_date: "2022-08-30T05:20:29Z",
    create_user: 56,
    update_date: "2022-08-30T05:20:31Z",
    update_user: 65,
    obsolete: 96,
    comments: "In iure et quibusdam",
    ta1_alias:
      "Ullam laboris elit sunt unde aliqua Adipisicing quis aspernatur at placeat voluptate",
    ta2_alias: "Ut accusamus non atque magni atque",
    ta3_alias:
      "Enim distinctio Id similique eu nihil sit architecto quo nesciunt qui quis cum aut et quibusdam molestiae",
    ta4_alias: "Vitae nostrud sit eos aut",
    ta5_alias:
      "Fuga Dolorum non dolor a consequuntur quia repudiandae velit reiciendis consectetur quidem duis vitae iure possimus magnam aut itaque cum",
    ta6_alias:
      "Sit voluptate laboris est mollit quos dolore quo aliquam consectetur molestias",
    ta7_alias:
      "Corrupti sed totam ea optio iusto iste similique Nam rerum veniam deleniti quis sed cillum quasi ducimus praesentium quo",
    ta8_alias:
      "Aut qui qui ipsum alias ipsum sed id quasi sint neque libero incididunt exercitationem consequatur Illo delectus vel iure ut",
    ta9_alias:
      "Accusamus voluptatem voluptas dolor ex ipsa ipsa vel magnam voluptas dolore officia fugit illum odit a fugiat veritatis quaerat",
    ta10_alias: "Amet rerum id non voluptatum ut molestias velit cillum",
    ta11_alias:
      "Corporis voluptatum dolor minima in explicabo Quia doloremque eius lorem est qui tempor saepe voluptatem",
    ta12_alias:
      "Architecto soluta laboriosam sunt distinctio Sit laborum Enim reprehenderit distinctio Anim",
    ta13_alias: "Elit numquam aliquam ut doloremque fugiat suscipit omnis",
    ta14_alias:
      "Ut ut reprehenderit nostrud provident qui consequat Id molestiae ipsum ea obcaecati",
    ta15_alias: "Nisi ea numquam nulla sunt labore ad elit",
    ta16_alias: "Rerum consequuntur sapiente aute aut et et velit iure",
    ta17_alias: "Eius illo fugiat velit sint voluptatem Et quidem",
    ta18_alias: "Error pariatur Dolor aperiam eos placeat consectetur",
    ta19_alias:
      "Est est minim impedit quis quis sit eos corrupti fugiat non aliquid nemo sit molestiae",
    ta20_alias: "Velit autem iusto amet non iste deleniti debitis assumenda",
    sl1_alias:
      "Sit do aut in enim neque commodo dolore culpa qui suscipit eos id",
    sl1_list: 94,
    sl2_alias:
      "Ad fugiat sit non omnis voluptatem voluptatum ullam eligendi aliquid nulla excepteur odit est perspiciatis molestiae in totam nisi",
    sl2_list: 43,
    sl3_alias:
      "Consequatur rerum et velit quia eu rerum velit nihil consectetur et",
    sl3_list: 76,
    sl4_alias:
      "Eligendi voluptate necessitatibus excepteur enim accusamus perferendis ipsum",
    sl4_list: 62,
    sl5_alias: "Et a omnis quidem et",
    sl5_list: 49,
    sl6_alias: "Accusantium sunt dolor lorem fugit dolore",
    sl6_list: 72,
    sl7_alias:
      "Aliquam veritatis maxime provident obcaecati voluptates aut eos sed corrupti doloribus qui amet enim",
    sl7_list: 20,
    sl8_alias: "Veniam recusandae Accusamus quis officia voluptates",
    sl8_list: 95,
    sl9_alias:
      "Anim quia cumque nisi officia nulla in possimus id mollit esse a",
    sl9_list: 21,
    sl10_alias: "Quas dolorem eaque quia aliquip ut eligendi minim",
    sl10_list: 38,
    sl11_alias:
      "Assumenda sed esse et eum odio amet eu velit saepe dignissimos quisquam aperiam reprehenderit doloremque est maiores",
    sl11_list: 2,
    sl12_alias: "Id quia sit deserunt enim fuga Eveniet odio",
    sl12_list: 59,
    sl13_alias: "Adipisci maiores magni duis neque",
    sl13_list: 67,
    sl14_alias:
      "Laboris qui voluptatem et ut qui sunt ratione praesentium ut culpa fuga Doloribus ut",
    sl14_list: 77,
    sl15_alias:
      "Explicabo Veniam voluptate corporis quia architecto iure enim voluptate sint dolore et consequatur ut id",
    sl15_list: 56,
    sl16_alias:
      "Nesciunt maiores sed dolore odit ut quae voluptas cupidatat officiis delectus",
    sl16_list: 40,
    sl17_alias:
      "Sed incidunt necessitatibus recusandae Do delectus dolore earum incidunt voluptas dolore labore dolore quia laboris",
    sl17_list: 95,
    sl18_alias: "Fuga Fugiat adipisci sunt quia dolor nisi",
    sl18_list: 8,
    sl19_alias:
      "Fugit blanditiis officia quia architecto exercitationem rerum quis molestiae elit reprehenderit quas aute dolore",
    sl19_list: 15,
    sl20_alias: "Dolores suscipit itaque neque ex atque amet",
    sl20_list: 76,
    zip: "59257",
    guid: "test",
  },
  {
    id: 10,
    organization_id: 40,
    name: "Ankit",
    code: "Repellendus Nostrud aut dolorum repellendus Culp",
    city: "Porro laborum Quasi praesentium doloremque in dol",
    state: "Cum nostrud ullam doloremque nisi culpa cupidatat",
    country: "Dolore dolor ab sequi nulla omnis odio obcaecati e",
    status: "Consequatur A explicabo Magna ut duis sint accus",
    create_date: "2022-08-30T05:20:29Z",
    create_user: 56,
    update_date: "2022-08-30T05:20:31Z",
    update_user: 65,
    obsolete: 96,
    comments: "In iure et quibusdam",
    ta1_alias:
      "Ullam laboris elit sunt unde aliqua Adipisicing quis aspernatur at placeat voluptate",
    ta2_alias: "Ut accusamus non atque magni atque",
    ta3_alias:
      "Enim distinctio Id similique eu nihil sit architecto quo nesciunt qui quis cum aut et quibusdam molestiae",
    ta4_alias: "Vitae nostrud sit eos aut",
    ta5_alias:
      "Fuga Dolorum non dolor a consequuntur quia repudiandae velit reiciendis consectetur quidem duis vitae iure possimus magnam aut itaque cum",
    ta6_alias:
      "Sit voluptate laboris est mollit quos dolore quo aliquam consectetur molestias",
    ta7_alias:
      "Corrupti sed totam ea optio iusto iste similique Nam rerum veniam deleniti quis sed cillum quasi ducimus praesentium quo",
    ta8_alias:
      "Aut qui qui ipsum alias ipsum sed id quasi sint neque libero incididunt exercitationem consequatur Illo delectus vel iure ut",
    ta9_alias:
      "Accusamus voluptatem voluptas dolor ex ipsa ipsa vel magnam voluptas dolore officia fugit illum odit a fugiat veritatis quaerat",
    ta10_alias: "Amet rerum id non voluptatum ut molestias velit cillum",
    ta11_alias:
      "Corporis voluptatum dolor minima in explicabo Quia doloremque eius lorem est qui tempor saepe voluptatem",
    ta12_alias:
      "Architecto soluta laboriosam sunt distinctio Sit laborum Enim reprehenderit distinctio Anim",
    ta13_alias: "Elit numquam aliquam ut doloremque fugiat suscipit omnis",
    ta14_alias:
      "Ut ut reprehenderit nostrud provident qui consequat Id molestiae ipsum ea obcaecati",
    ta15_alias: "Nisi ea numquam nulla sunt labore ad elit",
    ta16_alias: "Rerum consequuntur sapiente aute aut et et velit iure",
    ta17_alias: "Eius illo fugiat velit sint voluptatem Et quidem",
    ta18_alias: "Error pariatur Dolor aperiam eos placeat consectetur",
    ta19_alias:
      "Est est minim impedit quis quis sit eos corrupti fugiat non aliquid nemo sit molestiae",
    ta20_alias: "Velit autem iusto amet non iste deleniti debitis assumenda",
    sl1_alias:
      "Sit do aut in enim neque commodo dolore culpa qui suscipit eos id",
    sl1_list: 94,
    sl2_alias:
      "Ad fugiat sit non omnis voluptatem voluptatum ullam eligendi aliquid nulla excepteur odit est perspiciatis molestiae in totam nisi",
    sl2_list: 43,
    sl3_alias:
      "Consequatur rerum et velit quia eu rerum velit nihil consectetur et",
    sl3_list: 76,
    sl4_alias:
      "Eligendi voluptate necessitatibus excepteur enim accusamus perferendis ipsum",
    sl4_list: 62,
    sl5_alias: "Et a omnis quidem et",
    sl5_list: 49,
    sl6_alias: "Accusantium sunt dolor lorem fugit dolore",
    sl6_list: 72,
    sl7_alias:
      "Aliquam veritatis maxime provident obcaecati voluptates aut eos sed corrupti doloribus qui amet enim",
    sl7_list: 20,
    sl8_alias: "Veniam recusandae Accusamus quis officia voluptates",
    sl8_list: 95,
    sl9_alias:
      "Anim quia cumque nisi officia nulla in possimus id mollit esse a",
    sl9_list: 21,
    sl10_alias: "Quas dolorem eaque quia aliquip ut eligendi minim",
    sl10_list: 38,
    sl11_alias:
      "Assumenda sed esse et eum odio amet eu velit saepe dignissimos quisquam aperiam reprehenderit doloremque est maiores",
    sl11_list: 2,
    sl12_alias: "Id quia sit deserunt enim fuga Eveniet odio",
    sl12_list: 59,
    sl13_alias: "Adipisci maiores magni duis neque",
    sl13_list: 67,
    sl14_alias:
      "Laboris qui voluptatem et ut qui sunt ratione praesentium ut culpa fuga Doloribus ut",
    sl14_list: 77,
    sl15_alias:
      "Explicabo Veniam voluptate corporis quia architecto iure enim voluptate sint dolore et consequatur ut id",
    sl15_list: 56,
    sl16_alias:
      "Nesciunt maiores sed dolore odit ut quae voluptas cupidatat officiis delectus",
    sl16_list: 40,
    sl17_alias:
      "Sed incidunt necessitatibus recusandae Do delectus dolore earum incidunt voluptas dolore labore dolore quia laboris",
    sl17_list: 95,
    sl18_alias: "Fuga Fugiat adipisci sunt quia dolor nisi",
    sl18_list: 8,
    sl19_alias:
      "Fugit blanditiis officia quia architecto exercitationem rerum quis molestiae elit reprehenderit quas aute dolore",
    sl19_list: 15,
    sl20_alias: "Dolores suscipit itaque neque ex atque amet",
    sl20_list: 76,
    zip: "59257",
    guid: "test",
  },
  {
    id: 11,
    organization_id: 40,
    name: "Ankit",
    code: "Repellendus Nostrud aut dolorum repellendus Culp",
    city: "Porro laborum Quasi praesentium doloremque in dol",
    state: "Cum nostrud ullam doloremque nisi culpa cupidatat",
    country: "Dolore dolor ab sequi nulla omnis odio obcaecati e",
    status: "Consequatur A explicabo Magna ut duis sint accus",
    create_date: "2022-08-30T05:20:29Z",
    create_user: 56,
    update_date: "2022-08-30T05:20:31Z",
    update_user: 65,
    obsolete: 96,
    comments: "In iure et quibusdam",
    ta1_alias:
      "Ullam laboris elit sunt unde aliqua Adipisicing quis aspernatur at placeat voluptate",
    ta2_alias: "Ut accusamus non atque magni atque",
    ta3_alias:
      "Enim distinctio Id similique eu nihil sit architecto quo nesciunt qui quis cum aut et quibusdam molestiae",
    ta4_alias: "Vitae nostrud sit eos aut",
    ta5_alias:
      "Fuga Dolorum non dolor a consequuntur quia repudiandae velit reiciendis consectetur quidem duis vitae iure possimus magnam aut itaque cum",
    ta6_alias:
      "Sit voluptate laboris est mollit quos dolore quo aliquam consectetur molestias",
    ta7_alias:
      "Corrupti sed totam ea optio iusto iste similique Nam rerum veniam deleniti quis sed cillum quasi ducimus praesentium quo",
    ta8_alias:
      "Aut qui qui ipsum alias ipsum sed id quasi sint neque libero incididunt exercitationem consequatur Illo delectus vel iure ut",
    ta9_alias:
      "Accusamus voluptatem voluptas dolor ex ipsa ipsa vel magnam voluptas dolore officia fugit illum odit a fugiat veritatis quaerat",
    ta10_alias: "Amet rerum id non voluptatum ut molestias velit cillum",
    ta11_alias:
      "Corporis voluptatum dolor minima in explicabo Quia doloremque eius lorem est qui tempor saepe voluptatem",
    ta12_alias:
      "Architecto soluta laboriosam sunt distinctio Sit laborum Enim reprehenderit distinctio Anim",
    ta13_alias: "Elit numquam aliquam ut doloremque fugiat suscipit omnis",
    ta14_alias:
      "Ut ut reprehenderit nostrud provident qui consequat Id molestiae ipsum ea obcaecati",
    ta15_alias: "Nisi ea numquam nulla sunt labore ad elit",
    ta16_alias: "Rerum consequuntur sapiente aute aut et et velit iure",
    ta17_alias: "Eius illo fugiat velit sint voluptatem Et quidem",
    ta18_alias: "Error pariatur Dolor aperiam eos placeat consectetur",
    ta19_alias:
      "Est est minim impedit quis quis sit eos corrupti fugiat non aliquid nemo sit molestiae",
    ta20_alias: "Velit autem iusto amet non iste deleniti debitis assumenda",
    sl1_alias:
      "Sit do aut in enim neque commodo dolore culpa qui suscipit eos id",
    sl1_list: 94,
    sl2_alias:
      "Ad fugiat sit non omnis voluptatem voluptatum ullam eligendi aliquid nulla excepteur odit est perspiciatis molestiae in totam nisi",
    sl2_list: 43,
    sl3_alias:
      "Consequatur rerum et velit quia eu rerum velit nihil consectetur et",
    sl3_list: 76,
    sl4_alias:
      "Eligendi voluptate necessitatibus excepteur enim accusamus perferendis ipsum",
    sl4_list: 62,
    sl5_alias: "Et a omnis quidem et",
    sl5_list: 49,
    sl6_alias: "Accusantium sunt dolor lorem fugit dolore",
    sl6_list: 72,
    sl7_alias:
      "Aliquam veritatis maxime provident obcaecati voluptates aut eos sed corrupti doloribus qui amet enim",
    sl7_list: 20,
    sl8_alias: "Veniam recusandae Accusamus quis officia voluptates",
    sl8_list: 95,
    sl9_alias:
      "Anim quia cumque nisi officia nulla in possimus id mollit esse a",
    sl9_list: 21,
    sl10_alias: "Quas dolorem eaque quia aliquip ut eligendi minim",
    sl10_list: 38,
    sl11_alias:
      "Assumenda sed esse et eum odio amet eu velit saepe dignissimos quisquam aperiam reprehenderit doloremque est maiores",
    sl11_list: 2,
    sl12_alias: "Id quia sit deserunt enim fuga Eveniet odio",
    sl12_list: 59,
    sl13_alias: "Adipisci maiores magni duis neque",
    sl13_list: 67,
    sl14_alias:
      "Laboris qui voluptatem et ut qui sunt ratione praesentium ut culpa fuga Doloribus ut",
    sl14_list: 77,
    sl15_alias:
      "Explicabo Veniam voluptate corporis quia architecto iure enim voluptate sint dolore et consequatur ut id",
    sl15_list: 56,
    sl16_alias:
      "Nesciunt maiores sed dolore odit ut quae voluptas cupidatat officiis delectus",
    sl16_list: 40,
    sl17_alias:
      "Sed incidunt necessitatibus recusandae Do delectus dolore earum incidunt voluptas dolore labore dolore quia laboris",
    sl17_list: 95,
    sl18_alias: "Fuga Fugiat adipisci sunt quia dolor nisi",
    sl18_list: 8,
    sl19_alias:
      "Fugit blanditiis officia quia architecto exercitationem rerum quis molestiae elit reprehenderit quas aute dolore",
    sl19_list: 15,
    sl20_alias: "Dolores suscipit itaque neque ex atque amet",
    sl20_list: 76,
    zip: "59257",
    guid: "test",
  },
  {
    id: 12,
    organization_id: 40,
    name: "Ankit",
    code: "Repellendus Nostrud aut dolorum repellendus Culp",
    city: "Porro laborum Quasi praesentium doloremque in dol",
    state: "Cum nostrud ullam doloremque nisi culpa cupidatat",
    country: "Dolore dolor ab sequi nulla omnis odio obcaecati e",
    status: "Consequatur A explicabo Magna ut duis sint accus",
    create_date: "2022-08-30T05:20:29Z",
    create_user: 56,
    update_date: "2022-08-30T05:20:31Z",
    update_user: 65,
    obsolete: 96,
    comments: "In iure et quibusdam",
    ta1_alias:
      "Ullam laboris elit sunt unde aliqua Adipisicing quis aspernatur at placeat voluptate",
    ta2_alias: "Ut accusamus non atque magni atque",
    ta3_alias:
      "Enim distinctio Id similique eu nihil sit architecto quo nesciunt qui quis cum aut et quibusdam molestiae",
    ta4_alias: "Vitae nostrud sit eos aut",
    ta5_alias:
      "Fuga Dolorum non dolor a consequuntur quia repudiandae velit reiciendis consectetur quidem duis vitae iure possimus magnam aut itaque cum",
    ta6_alias:
      "Sit voluptate laboris est mollit quos dolore quo aliquam consectetur molestias",
    ta7_alias:
      "Corrupti sed totam ea optio iusto iste similique Nam rerum veniam deleniti quis sed cillum quasi ducimus praesentium quo",
    ta8_alias:
      "Aut qui qui ipsum alias ipsum sed id quasi sint neque libero incididunt exercitationem consequatur Illo delectus vel iure ut",
    ta9_alias:
      "Accusamus voluptatem voluptas dolor ex ipsa ipsa vel magnam voluptas dolore officia fugit illum odit a fugiat veritatis quaerat",
    ta10_alias: "Amet rerum id non voluptatum ut molestias velit cillum",
    ta11_alias:
      "Corporis voluptatum dolor minima in explicabo Quia doloremque eius lorem est qui tempor saepe voluptatem",
    ta12_alias:
      "Architecto soluta laboriosam sunt distinctio Sit laborum Enim reprehenderit distinctio Anim",
    ta13_alias: "Elit numquam aliquam ut doloremque fugiat suscipit omnis",
    ta14_alias:
      "Ut ut reprehenderit nostrud provident qui consequat Id molestiae ipsum ea obcaecati",
    ta15_alias: "Nisi ea numquam nulla sunt labore ad elit",
    ta16_alias: "Rerum consequuntur sapiente aute aut et et velit iure",
    ta17_alias: "Eius illo fugiat velit sint voluptatem Et quidem",
    ta18_alias: "Error pariatur Dolor aperiam eos placeat consectetur",
    ta19_alias:
      "Est est minim impedit quis quis sit eos corrupti fugiat non aliquid nemo sit molestiae",
    ta20_alias: "Velit autem iusto amet non iste deleniti debitis assumenda",
    sl1_alias:
      "Sit do aut in enim neque commodo dolore culpa qui suscipit eos id",
    sl1_list: 94,
    sl2_alias:
      "Ad fugiat sit non omnis voluptatem voluptatum ullam eligendi aliquid nulla excepteur odit est perspiciatis molestiae in totam nisi",
    sl2_list: 43,
    sl3_alias:
      "Consequatur rerum et velit quia eu rerum velit nihil consectetur et",
    sl3_list: 76,
    sl4_alias:
      "Eligendi voluptate necessitatibus excepteur enim accusamus perferendis ipsum",
    sl4_list: 62,
    sl5_alias: "Et a omnis quidem et",
    sl5_list: 49,
    sl6_alias: "Accusantium sunt dolor lorem fugit dolore",
    sl6_list: 72,
    sl7_alias:
      "Aliquam veritatis maxime provident obcaecati voluptates aut eos sed corrupti doloribus qui amet enim",
    sl7_list: 20,
    sl8_alias: "Veniam recusandae Accusamus quis officia voluptates",
    sl8_list: 95,
    sl9_alias:
      "Anim quia cumque nisi officia nulla in possimus id mollit esse a",
    sl9_list: 21,
    sl10_alias: "Quas dolorem eaque quia aliquip ut eligendi minim",
    sl10_list: 38,
    sl11_alias:
      "Assumenda sed esse et eum odio amet eu velit saepe dignissimos quisquam aperiam reprehenderit doloremque est maiores",
    sl11_list: 2,
    sl12_alias: "Id quia sit deserunt enim fuga Eveniet odio",
    sl12_list: 59,
    sl13_alias: "Adipisci maiores magni duis neque",
    sl13_list: 67,
    sl14_alias:
      "Laboris qui voluptatem et ut qui sunt ratione praesentium ut culpa fuga Doloribus ut",
    sl14_list: 77,
    sl15_alias:
      "Explicabo Veniam voluptate corporis quia architecto iure enim voluptate sint dolore et consequatur ut id",
    sl15_list: 56,
    sl16_alias:
      "Nesciunt maiores sed dolore odit ut quae voluptas cupidatat officiis delectus",
    sl16_list: 40,
    sl17_alias:
      "Sed incidunt necessitatibus recusandae Do delectus dolore earum incidunt voluptas dolore labore dolore quia laboris",
    sl17_list: 95,
    sl18_alias: "Fuga Fugiat adipisci sunt quia dolor nisi",
    sl18_list: 8,
    sl19_alias:
      "Fugit blanditiis officia quia architecto exercitationem rerum quis molestiae elit reprehenderit quas aute dolore",
    sl19_list: 15,
    sl20_alias: "Dolores suscipit itaque neque ex atque amet",
    sl20_list: 76,
    zip: "59257",
    guid: "test",
  },
  {
    id: 13,
    organization_id: 40,
    name: "Ankit",
    code: "Repellendus Nostrud aut dolorum repellendus Culp",
    city: "Porro laborum Quasi praesentium doloremque in dol",
    state: "Cum nostrud ullam doloremque nisi culpa cupidatat",
    country: "Dolore dolor ab sequi nulla omnis odio obcaecati e",
    status: "Consequatur A explicabo Magna ut duis sint accus",
    create_date: "2022-08-30T05:20:29Z",
    create_user: 56,
    update_date: "2022-08-30T05:20:31Z",
    update_user: 65,
    obsolete: 96,
    comments: "In iure et quibusdam",
    ta1_alias:
      "Ullam laboris elit sunt unde aliqua Adipisicing quis aspernatur at placeat voluptate",
    ta2_alias: "Ut accusamus non atque magni atque",
    ta3_alias:
      "Enim distinctio Id similique eu nihil sit architecto quo nesciunt qui quis cum aut et quibusdam molestiae",
    ta4_alias: "Vitae nostrud sit eos aut",
    ta5_alias:
      "Fuga Dolorum non dolor a consequuntur quia repudiandae velit reiciendis consectetur quidem duis vitae iure possimus magnam aut itaque cum",
    ta6_alias:
      "Sit voluptate laboris est mollit quos dolore quo aliquam consectetur molestias",
    ta7_alias:
      "Corrupti sed totam ea optio iusto iste similique Nam rerum veniam deleniti quis sed cillum quasi ducimus praesentium quo",
    ta8_alias:
      "Aut qui qui ipsum alias ipsum sed id quasi sint neque libero incididunt exercitationem consequatur Illo delectus vel iure ut",
    ta9_alias:
      "Accusamus voluptatem voluptas dolor ex ipsa ipsa vel magnam voluptas dolore officia fugit illum odit a fugiat veritatis quaerat",
    ta10_alias: "Amet rerum id non voluptatum ut molestias velit cillum",
    ta11_alias:
      "Corporis voluptatum dolor minima in explicabo Quia doloremque eius lorem est qui tempor saepe voluptatem",
    ta12_alias:
      "Architecto soluta laboriosam sunt distinctio Sit laborum Enim reprehenderit distinctio Anim",
    ta13_alias: "Elit numquam aliquam ut doloremque fugiat suscipit omnis",
    ta14_alias:
      "Ut ut reprehenderit nostrud provident qui consequat Id molestiae ipsum ea obcaecati",
    ta15_alias: "Nisi ea numquam nulla sunt labore ad elit",
    ta16_alias: "Rerum consequuntur sapiente aute aut et et velit iure",
    ta17_alias: "Eius illo fugiat velit sint voluptatem Et quidem",
    ta18_alias: "Error pariatur Dolor aperiam eos placeat consectetur",
    ta19_alias:
      "Est est minim impedit quis quis sit eos corrupti fugiat non aliquid nemo sit molestiae",
    ta20_alias: "Velit autem iusto amet non iste deleniti debitis assumenda",
    sl1_alias:
      "Sit do aut in enim neque commodo dolore culpa qui suscipit eos id",
    sl1_list: 94,
    sl2_alias:
      "Ad fugiat sit non omnis voluptatem voluptatum ullam eligendi aliquid nulla excepteur odit est perspiciatis molestiae in totam nisi",
    sl2_list: 43,
    sl3_alias:
      "Consequatur rerum et velit quia eu rerum velit nihil consectetur et",
    sl3_list: 76,
    sl4_alias:
      "Eligendi voluptate necessitatibus excepteur enim accusamus perferendis ipsum",
    sl4_list: 62,
    sl5_alias: "Et a omnis quidem et",
    sl5_list: 49,
    sl6_alias: "Accusantium sunt dolor lorem fugit dolore",
    sl6_list: 72,
    sl7_alias:
      "Aliquam veritatis maxime provident obcaecati voluptates aut eos sed corrupti doloribus qui amet enim",
    sl7_list: 20,
    sl8_alias: "Veniam recusandae Accusamus quis officia voluptates",
    sl8_list: 95,
    sl9_alias:
      "Anim quia cumque nisi officia nulla in possimus id mollit esse a",
    sl9_list: 21,
    sl10_alias: "Quas dolorem eaque quia aliquip ut eligendi minim",
    sl10_list: 38,
    sl11_alias:
      "Assumenda sed esse et eum odio amet eu velit saepe dignissimos quisquam aperiam reprehenderit doloremque est maiores",
    sl11_list: 2,
    sl12_alias: "Id quia sit deserunt enim fuga Eveniet odio",
    sl12_list: 59,
    sl13_alias: "Adipisci maiores magni duis neque",
    sl13_list: 67,
    sl14_alias:
      "Laboris qui voluptatem et ut qui sunt ratione praesentium ut culpa fuga Doloribus ut",
    sl14_list: 77,
    sl15_alias:
      "Explicabo Veniam voluptate corporis quia architecto iure enim voluptate sint dolore et consequatur ut id",
    sl15_list: 56,
    sl16_alias:
      "Nesciunt maiores sed dolore odit ut quae voluptas cupidatat officiis delectus",
    sl16_list: 40,
    sl17_alias:
      "Sed incidunt necessitatibus recusandae Do delectus dolore earum incidunt voluptas dolore labore dolore quia laboris",
    sl17_list: 95,
    sl18_alias: "Fuga Fugiat adipisci sunt quia dolor nisi",
    sl18_list: 8,
    sl19_alias:
      "Fugit blanditiis officia quia architecto exercitationem rerum quis molestiae elit reprehenderit quas aute dolore",
    sl19_list: 15,
    sl20_alias: "Dolores suscipit itaque neque ex atque amet",
    sl20_list: 76,
    zip: "59257",
    guid: "test",
  },
  {
    id: 14,
    organization_id: 40,
    name: "Ankit",
    code: "Repellendus Nostrud aut dolorum repellendus Culp",
    city: "Porro laborum Quasi praesentium doloremque in dol",
    state: "Cum nostrud ullam doloremque nisi culpa cupidatat",
    country: "Dolore dolor ab sequi nulla omnis odio obcaecati e",
    status: "Consequatur A explicabo Magna ut duis sint accus",
    create_date: "2022-08-30T05:20:29Z",
    create_user: 56,
    update_date: "2022-08-30T05:20:31Z",
    update_user: 65,
    obsolete: 96,
    comments: "In iure et quibusdam",
    ta1_alias:
      "Ullam laboris elit sunt unde aliqua Adipisicing quis aspernatur at placeat voluptate",
    ta2_alias: "Ut accusamus non atque magni atque",
    ta3_alias:
      "Enim distinctio Id similique eu nihil sit architecto quo nesciunt qui quis cum aut et quibusdam molestiae",
    ta4_alias: "Vitae nostrud sit eos aut",
    ta5_alias:
      "Fuga Dolorum non dolor a consequuntur quia repudiandae velit reiciendis consectetur quidem duis vitae iure possimus magnam aut itaque cum",
    ta6_alias:
      "Sit voluptate laboris est mollit quos dolore quo aliquam consectetur molestias",
    ta7_alias:
      "Corrupti sed totam ea optio iusto iste similique Nam rerum veniam deleniti quis sed cillum quasi ducimus praesentium quo",
    ta8_alias:
      "Aut qui qui ipsum alias ipsum sed id quasi sint neque libero incididunt exercitationem consequatur Illo delectus vel iure ut",
    ta9_alias:
      "Accusamus voluptatem voluptas dolor ex ipsa ipsa vel magnam voluptas dolore officia fugit illum odit a fugiat veritatis quaerat",
    ta10_alias: "Amet rerum id non voluptatum ut molestias velit cillum",
    ta11_alias:
      "Corporis voluptatum dolor minima in explicabo Quia doloremque eius lorem est qui tempor saepe voluptatem",
    ta12_alias:
      "Architecto soluta laboriosam sunt distinctio Sit laborum Enim reprehenderit distinctio Anim",
    ta13_alias: "Elit numquam aliquam ut doloremque fugiat suscipit omnis",
    ta14_alias:
      "Ut ut reprehenderit nostrud provident qui consequat Id molestiae ipsum ea obcaecati",
    ta15_alias: "Nisi ea numquam nulla sunt labore ad elit",
    ta16_alias: "Rerum consequuntur sapiente aute aut et et velit iure",
    ta17_alias: "Eius illo fugiat velit sint voluptatem Et quidem",
    ta18_alias: "Error pariatur Dolor aperiam eos placeat consectetur",
    ta19_alias:
      "Est est minim impedit quis quis sit eos corrupti fugiat non aliquid nemo sit molestiae",
    ta20_alias: "Velit autem iusto amet non iste deleniti debitis assumenda",
    sl1_alias:
      "Sit do aut in enim neque commodo dolore culpa qui suscipit eos id",
    sl1_list: 94,
    sl2_alias:
      "Ad fugiat sit non omnis voluptatem voluptatum ullam eligendi aliquid nulla excepteur odit est perspiciatis molestiae in totam nisi",
    sl2_list: 43,
    sl3_alias:
      "Consequatur rerum et velit quia eu rerum velit nihil consectetur et",
    sl3_list: 76,
    sl4_alias:
      "Eligendi voluptate necessitatibus excepteur enim accusamus perferendis ipsum",
    sl4_list: 62,
    sl5_alias: "Et a omnis quidem et",
    sl5_list: 49,
    sl6_alias: "Accusantium sunt dolor lorem fugit dolore",
    sl6_list: 72,
    sl7_alias:
      "Aliquam veritatis maxime provident obcaecati voluptates aut eos sed corrupti doloribus qui amet enim",
    sl7_list: 20,
    sl8_alias: "Veniam recusandae Accusamus quis officia voluptates",
    sl8_list: 95,
    sl9_alias:
      "Anim quia cumque nisi officia nulla in possimus id mollit esse a",
    sl9_list: 21,
    sl10_alias: "Quas dolorem eaque quia aliquip ut eligendi minim",
    sl10_list: 38,
    sl11_alias:
      "Assumenda sed esse et eum odio amet eu velit saepe dignissimos quisquam aperiam reprehenderit doloremque est maiores",
    sl11_list: 2,
    sl12_alias: "Id quia sit deserunt enim fuga Eveniet odio",
    sl12_list: 59,
    sl13_alias: "Adipisci maiores magni duis neque",
    sl13_list: 67,
    sl14_alias:
      "Laboris qui voluptatem et ut qui sunt ratione praesentium ut culpa fuga Doloribus ut",
    sl14_list: 77,
    sl15_alias:
      "Explicabo Veniam voluptate corporis quia architecto iure enim voluptate sint dolore et consequatur ut id",
    sl15_list: 56,
    sl16_alias:
      "Nesciunt maiores sed dolore odit ut quae voluptas cupidatat officiis delectus",
    sl16_list: 40,
    sl17_alias:
      "Sed incidunt necessitatibus recusandae Do delectus dolore earum incidunt voluptas dolore labore dolore quia laboris",
    sl17_list: 95,
    sl18_alias: "Fuga Fugiat adipisci sunt quia dolor nisi",
    sl18_list: 8,
    sl19_alias:
      "Fugit blanditiis officia quia architecto exercitationem rerum quis molestiae elit reprehenderit quas aute dolore",
    sl19_list: 15,
    sl20_alias: "Dolores suscipit itaque neque ex atque amet",
    sl20_list: 76,
    zip: "59257",
    guid: "test",
  },
  {
    id: 15,
    organization_id: 28,
    name: "Jordan Guy",
    code: "Deleniti eius ex nulla non autem id veniam velit",
    city: "Animi fugiat iure obcaecati recusandae Nostrum e",
    state: "Consequuntur cupiditate in cumque doloribus",
    country: "Saepe velit velit veniam sapiente culpa quos",
    status: "Velit et lorem est minima molestiae maxime et vo",
    create_date: null,
    create_user: 76,
    update_date: null,
    update_user: 33,
    obsolete: 12,
    comments: "Corporis nostrum mag",
    ta1_alias:
      "Quaerat dolore qui possimus ad consequat Cillum dicta in iste qui dolore et dolore asperiores possimus adipisci vitae amet tempora",
    ta2_alias:
      "Odit sit dolore officiis dolore voluptatem ratione provident officia nulla",
    ta3_alias:
      "Vel voluptas quam voluptatem Commodi irure laborum Elit explicabo Adipisci duis consequatur culpa earum voluptatem id",
    ta4_alias:
      "Eius id recusandae Et qui ex quis culpa libero laudantium ut dolore est quos aspernatur voluptas similique voluptatem Rerum",
    ta5_alias:
      "Eum dignissimos voluptates nihil velit modi enim quam quas dolor id magna enim id",
    ta6_alias:
      "Maiores do animi iusto quo sed officia rem quos consequatur quasi consequuntur elit",
    ta7_alias:
      "Beatae quam possimus nulla ullam laboris ad dolorem aliqua Adipisicing qui similique nisi",
    ta8_alias:
      "Ut ut quo doloremque consequatur Perspiciatis fugiat totam numquam commodo sequi aut",
    ta9_alias:
      "Tempore amet pariatur Culpa consectetur minima eum qui est ea excepturi non dolor in veritatis sit deleniti eiusmod explicabo Quibusdam",
    ta10_alias:
      "Aut ea soluta modi facere aute quia dignissimos rerum quis iste in tempora sint aut laborum Sint dignissimos",
    ta11_alias: "Est quia quasi amet dolor deserunt quo quia est eaque",
    ta12_alias:
      "Ea proident doloremque autem exercitationem non enim facere aut non alias distinctio Dignissimos qui culpa",
    ta13_alias: "Necessitatibus blanditiis porro officiis optio anim quam",
    ta14_alias: "Officia voluptas illo est sit",
    ta15_alias: "Consequuntur et assumenda est in repudiandae",
    ta16_alias:
      "Nesciunt libero aut et in velit ad hic dolorum magna distinctio Quia pariatur Voluptate lorem nisi nostrud",
    ta17_alias:
      "Pariatur Esse ut omnis molestiae aliquam iure dolor sed proident sequi aut sit ut culpa exercitation sit",
    ta18_alias:
      "Alias officia cumque id reprehenderit aliqua Expedita in consequuntur nulla blanditiis aliquip aut possimus",
    ta19_alias:
      "Mollitia elit ut est nesciunt molestias assumenda aut voluptatem quo nihil accusantium quis voluptate consequat Et molestias totam",
    ta20_alias:
      "Numquam laboris et quibusdam minus aut facilis perferendis sint amet elit id eius eveniet iusto earum quia",
    sl1_alias: "Aut suscipit velit commodo rerum",
    sl1_list: 3,
    sl2_alias:
      "Asperiores iste est sint cillum est sequi rerum maxime deleniti quae aut aut rerum in eiusmod distinctio Et",
    sl2_list: 93,
    sl3_alias:
      "Cillum provident fugit voluptate id sed possimus eu expedita sit proident explicabo Eligendi nostrum eos id",
    sl3_list: 64,
    sl4_alias: "Est sapiente et molestiae enim",
    sl4_list: 86,
    sl5_alias: "Sed sed aspernatur necessitatibus ipsa sequi",
    sl5_list: 30,
    sl6_alias:
      "Est delectus rerum provident illum aut repellendus Aut dolores explicabo Accusamus proident nihil voluptas culpa iste delectus autem",
    sl6_list: 65,
    sl7_alias:
      "Velit reprehenderit quaerat atque eveniet in aperiam dolores autem nesciunt labore praesentium doloremque recusandae Aliquid ullamco libero in cupiditate",
    sl7_list: 81,
    sl8_alias: "Itaque officiis officiis occaecat earum",
    sl8_list: 72,
    sl9_alias:
      "Fugiat et repudiandae incididunt odio perferendis labore ex quod",
    sl9_list: 57,
    sl10_alias: "Expedita distinctio Sunt animi est voluptate cum animi",
    sl10_list: 33,
    sl11_alias: "Est autem placeat magnam dolor velit a",
    sl11_list: 93,
    sl12_alias:
      "Temporibus molestias ad enim fugiat voluptates recusandae Cupidatat porro magni est quia duis adipisicing numquam sit esse proident ipsa",
    sl12_list: 53,
    sl13_alias:
      "Tempora numquam magna repudiandae nulla veniam aut ut dolor laboris est recusandae Deserunt ipsa nobis fugiat voluptatum tempora molestias",
    sl13_list: 16,
    sl14_alias:
      "Voluptas voluptatem obcaecati qui dolorum accusantium minima delectus aliquid sed accusamus labore do qui fugiat",
    sl14_list: 17,
    sl15_alias:
      "Quam eum officia nobis non eum tempor provident pariatur Impedit et non",
    sl15_list: 63,
    sl16_alias:
      "Minima nisi quaerat rerum ut recusandae Ut alias dolore quod unde nesciunt aliquip at modi in alias",
    sl16_list: 84,
    sl17_alias:
      "Consectetur aliqua Quia elit qui est labore esse excepteur asperiores molestias inventore quaerat numquam cum et",
    sl17_list: 58,
    sl18_alias:
      "Quidem qui rem totam veniam laborum Repellendus Natus beatae dolor adipisicing aliqua In ut vel impedit aut",
    sl18_list: 67,
    sl19_alias:
      "Quia eum veniam ex vero aut quibusdam omnis in architecto nulla et",
    sl19_list: 22,
    sl20_alias: "A ut consectetur incididunt dolores ad",
    sl20_list: 36,
    zip: "12841",
    guid: "Omnis magnam quo sit est non illum",
  },
  {
    id: 16,
    organization_id: 34,
    name: "Teegan Vazquez",
    code: "Labore esse enim consequatur enim exercitationem",
    city: "Incidunt recusandae Officia amet voluptas verit",
    state: "Ad dolores enim omnis assumenda eu laborum possimu",
    country: "Eos quis autem neque quos facere similique fugit",
    status: "Est suscipit quo in sit",
    create_date: null,
    create_user: 45,
    update_date: null,
    update_user: 33,
    obsolete: 86,
    comments: "Vel enim ad voluptat",
    ta1_alias:
      "Deserunt fugiat est quam placeat quidem voluptatum sit excepteur ullamco ut sit aspernatur dolor",
    ta2_alias: "Obcaecati iste quia eaque quod alias obcaecati velit ea non",
    ta3_alias:
      "Ratione voluptatum voluptatum inventore non exercitation facere molestiae voluptatibus et et porro porro",
    ta4_alias:
      "Nobis quidem ullam vero sed molestiae alias libero quia quod et corrupti aut quia sapiente",
    ta5_alias:
      "Facilis dolore excepturi vel ad in repellendus Pariatur Ea ea reprehenderit facere accusamus",
    ta6_alias:
      "Autem est minima quaerat qui molestias animi reprehenderit et deserunt eveniet ut nostrum porro",
    ta7_alias:
      "A accusamus sequi consequat Aliquid et qui placeat magni atque rerum dignissimos",
    ta8_alias:
      "Enim asperiores quidem sequi quod et ullam anim quae illum quas quia nesciunt pariatur Iure eum qui",
    ta9_alias:
      "Neque pariatur Ad tempor doloribus laborum aliquid harum doloribus architecto quam voluptatem consequuntur qui blanditiis",
    ta10_alias:
      "Est quisquam in adipisci Nam voluptatem sit qui eius tenetur atque excepteur deserunt elit omnis",
    ta11_alias:
      "Cupidatat neque obcaecati eu quod sed aliqua Tempora nisi autem velit harum",
    ta12_alias:
      "In maxime vel commodi possimus similique similique mollit a inventore est qui lorem deserunt commodo reiciendis illum eligendi proident quos",
    ta13_alias:
      "Fugiat ipsum in elit cupidatat nemo amet accusantium consequat Quo delectus deserunt qui praesentium totam est",
    ta14_alias: "Quos minima ut fuga Cupidatat ut cillum",
    ta15_alias:
      "Porro voluptate eos cupidatat vitae ducimus sit quos possimus qui dolor aliquam atque dolorem et enim quis et",
    ta16_alias: "Et maiores fuga Quisquam in",
    ta17_alias:
      "Ipsum sed adipisicing enim maxime molestiae consequatur Quo irure iusto vero",
    ta18_alias: "Placeat velit ut beatae alias ex",
    ta19_alias:
      "Qui enim consequat Culpa alias officia unde nobis quia consequatur Veniam consequatur Dolor",
    ta20_alias:
      "Libero delectus sit error quam cumque et qui dolore aut impedit ea irure odio iure sint est",
    sl1_alias:
      "Ad numquam totam facere accusamus proident aspernatur eaque incidunt dolore provident excepturi ea",
    sl1_list: 21,
    sl2_alias:
      "Veniam dolorum commodo ullamco officia fugit ad eum non elit sit aut fuga Cupiditate mollit sed nisi",
    sl2_list: 84,
    sl3_alias:
      "Minima sed necessitatibus laboriosam nihil id proident illum autem cum qui dolor amet fugit numquam harum ipsam",
    sl3_list: 73,
    sl4_alias:
      "Sequi ratione ut aliquid fuga Est quis lorem dolor quia illo sed iure fugiat qui est quo dolore",
    sl4_list: 5,
    sl5_alias: "Cum ut molestiae amet aliquam",
    sl5_list: 99,
    sl6_alias:
      "Nemo reiciendis voluptatum repellendus Consequatur in possimus assumenda est reiciendis fugiat ut",
    sl6_list: 62,
    sl7_alias:
      "Ratione praesentium distinctio Reprehenderit ea officia est qui ipsam qui voluptate in mollit omnis illo",
    sl7_list: 76,
    sl8_alias:
      "Consectetur laborum Consequatur Facilis voluptate autem ut sed non animi dolorum sapiente",
    sl8_list: 9,
    sl9_alias:
      "Omnis reprehenderit incididunt Nam eaque earum sed sunt corporis eiusmod aut ad dolores pariatur Obcaecati provident sunt incididunt",
    sl9_list: 50,
    sl10_alias: "Anim modi eu dolore quo dolor dolores alias sit",
    sl10_list: 53,
    sl11_alias:
      "Doloribus quam ad enim harum laborum Tenetur quibusdam omnis magna animi incidunt cupidatat et non quaerat corporis maxime laboriosam",
    sl11_list: 24,
    sl12_alias:
      "Omnis corrupti mollitia ipsum aliqua Suscipit ut tempore iusto consectetur mollitia quaerat enim iure",
    sl12_list: 20,
    sl13_alias:
      "Praesentium optio enim quas rerum ut aut ut nostrud ipsum esse",
    sl13_list: 7,
    sl14_alias: "Vel ipsa aut officiis enim quia dolore",
    sl14_list: 3,
    sl15_alias: "Qui velit est quia recusandae Molestiae rerum dolor corrupti",
    sl15_list: 67,
    sl16_alias:
      "Ad tempor nihil ex et eius eu natus exercitation est mollitia et amet",
    sl16_list: 32,
    sl17_alias: "Culpa in lorem totam minim",
    sl17_list: 43,
    sl18_alias: "Illo ut ut id voluptate vero quo",
    sl18_list: 37,
    sl19_alias:
      "Fugiat impedit deleniti recusandae Repellendus Sint natus voluptate qui ea esse labore omnis vitae magna qui ipsam est quae aliquam",
    sl19_list: 96,
    sl20_alias:
      "Consequatur Eu non fuga Dolor aute et voluptatem sunt error tempor eligendi hic aliqua Et voluptate",
    sl20_list: 82,
    zip: "27052",
    guid: "Deserunt veniam perspiciatis conse",
  },
  {
    id: 17,
    organization_id: 90,
    name: "Anika Arnold",
    code: "Dolorum qui inventore dolor et voluptatem Exercit",
    city: "Dolor excepteur proident saepe aut impedit expli",
    state: "Aut nostrud quae nihil ea nisi quaerat quo",
    country: "Sed nostrum facilis ad quod iste soluta culpa labo",
    status: "Eum modi facilis alias sed molestias ipsa magni q",
    create_date: null,
    create_user: 68,
    update_date: null,
    update_user: 7,
    obsolete: 98,
    comments: "Quae magni voluptate",
    ta1_alias:
      "Unde laboris occaecat dignissimos unde cupiditate facilis sunt voluptas nostrud repellendus Fugit voluptas adipisicing",
    ta2_alias: "Aliquam adipisicing quia sunt quas in et ratione labore ut sed",
    ta3_alias:
      "Dicta voluptatibus ducimus cumque aute veritatis quia illo labore dolores velit ea velit",
    ta4_alias: "Voluptate itaque blanditiis aut aut sed dolorem",
    ta5_alias:
      "Cumque inventore quaerat sed ut praesentium exercitationem itaque sed amet qui voluptates eu pariatur Tempora ut et elit officia in",
    ta6_alias: "Quia non autem ducimus anim dolores qui exercitationem quo",
    ta7_alias: "Similique quaerat qui hic delectus molestiae",
    ta8_alias:
      "Adipisci sed consequatur aut numquam adipisci eligendi sapiente enim",
    ta9_alias:
      "Odio repudiandae consequatur Pariatur In laborum molestiae est inventore lorem inventore modi",
    ta10_alias:
      "Et commodi qui ad porro et hic dolorem beatae quam qui fugit sunt molestiae",
    ta11_alias:
      "Amet voluptatibus autem et ducimus quaerat est repudiandae est aspernatur veniam aut non",
    ta12_alias:
      "Iure qui eius dolores aliquip ut error et officia qui et nostrud voluptatem non quia facilis",
    ta13_alias:
      "Et ut officiis id lorem est occaecat quisquam veniam aut earum aliqua Sunt iste eveniet et dolorum",
    ta14_alias:
      "Quis consequatur accusantium qui culpa temporibus magnam pariatur Id iure",
    ta15_alias:
      "Dolorem velit do alias rerum est ut velit lorem veniam voluptates eum quae",
    ta16_alias:
      "Id in elit quia at dolores autem quos natus non aspernatur occaecat quas",
    ta17_alias:
      "Et in maiores quia at quis ut placeat beatae non dolores consectetur harum soluta et aut blanditiis",
    ta18_alias:
      "Consectetur sit magnam ut necessitatibus asperiores molestiae eum fugit aliquam aut est ea molestiae consequuntur aliquip quis sit",
    ta19_alias:
      "Nesciunt sed ullamco voluptas reiciendis consectetur odio amet",
    ta20_alias:
      "Magni eu quia eveniet tempore nulla quia id blanditiis anim sint sunt fugiat reiciendis",
    sl1_alias:
      "Voluptatem Dolor dolor dolor quis veritatis dolore voluptas expedita in ut eum qui",
    sl1_list: 59,
    sl2_alias: "In qui quis cum deserunt",
    sl2_list: 53,
    sl3_alias:
      "Blanditiis corrupti culpa ad nobis quod doloremque sunt cumque quibusdam rem exercitation quis ex temporibus eaque",
    sl3_list: 8,
    sl4_alias:
      "Iure accusantium suscipit esse ex autem culpa nemo dolorem cupidatat quisquam qui",
    sl4_list: 33,
    sl5_alias: "Nesciunt eum ratione mollit laborum iure",
    sl5_list: 21,
    sl6_alias: "In aliquam dolor nulla consectetur",
    sl6_list: 93,
    sl7_alias: "Nostrud harum deserunt rem do cum voluptas",
    sl7_list: 36,
    sl8_alias:
      "Velit est nobis odit aut saepe vel temporibus illo architecto quia architecto in ea est ducimus non ab earum voluptatibus",
    sl8_list: 30,
    sl9_alias: "Tempora dolorem quia dicta earum laborum sunt provident",
    sl9_list: 72,
    sl10_alias: "Distinctio Vero commodi architecto qui quisquam est voluptate",
    sl10_list: 60,
    sl11_alias:
      "Nulla nisi doloremque ea doloribus reprehenderit esse unde voluptas illo vel nostrud esse non voluptas amet dicta tempor consequatur Aut",
    sl11_list: 78,
    sl12_alias:
      "Animi in et minus hic fugiat quos nostrud doloribus esse dolorem quibusdam error sit quia elit voluptas",
    sl12_list: 15,
    sl13_alias: "Possimus reprehenderit ex rerum aliquid repudiandae minima",
    sl13_list: 71,
    sl14_alias: "Dolor tenetur sed ad ex fugiat quasi et",
    sl14_list: 16,
    sl15_alias: "Et quo sunt quia ipsam quis",
    sl15_list: 74,
    sl16_alias:
      "Necessitatibus ipsum ipsum nostrud quae incididunt voluptas adipisci quisquam impedit dolorem",
    sl16_list: 95,
    sl17_alias:
      "Tempore voluptas ut non inventore ad velit et excepteur magnam perspiciatis labore commodo adipisci aliqua Labore",
    sl17_list: 98,
    sl18_alias:
      "Eiusmod tenetur in aut neque sit minima quod dolorem esse ex quas magni",
    sl18_list: 77,
    sl19_alias:
      "Labore tempora voluptate sit saepe officia et officiis velit ab amet quia",
    sl19_list: 18,
    sl20_alias: "Lorem est laborum Quo dolor sequi",
    sl20_list: 80,
    zip: "39438",
    guid: "Fugit nemo mollitia ipsum hic omni",
  },
  {
    id: 18,
    organization_id: null,
    name: null,
    code: null,
    city: null,
    state: null,
    country: null,
    status: null,
    create_date: null,
    create_user: null,
    update_date: null,
    update_user: null,
    obsolete: null,
    comments: null,
    ta1_alias: null,
    ta2_alias: null,
    ta3_alias: null,
    ta4_alias: null,
    ta5_alias: null,
    ta6_alias: null,
    ta7_alias: null,
    ta8_alias: null,
    ta9_alias: null,
    ta10_alias: null,
    ta11_alias: null,
    ta12_alias: null,
    ta13_alias: null,
    ta14_alias: null,
    ta15_alias: null,
    ta16_alias: null,
    ta17_alias: null,
    ta18_alias: null,
    ta19_alias: null,
    ta20_alias: null,
    sl1_alias: null,
    sl1_list: null,
    sl2_alias: null,
    sl2_list: null,
    sl3_alias: null,
    sl3_list: null,
    sl4_alias: null,
    sl4_list: null,
    sl5_alias: null,
    sl5_list: null,
    sl6_alias: null,
    sl6_list: null,
    sl7_alias: null,
    sl7_list: null,
    sl8_alias: null,
    sl8_list: null,
    sl9_alias: null,
    sl9_list: null,
    sl10_alias: null,
    sl10_list: null,
    sl11_alias: null,
    sl11_list: null,
    sl12_alias: null,
    sl12_list: null,
    sl13_alias: null,
    sl13_list: null,
    sl14_alias: null,
    sl14_list: null,
    sl15_alias: null,
    sl15_list: null,
    sl16_alias: null,
    sl16_list: null,
    sl17_alias: null,
    sl17_list: null,
    sl18_alias: null,
    sl18_list: null,
    sl19_alias: null,
    sl19_list: null,
    sl20_alias: null,
    sl20_list: null,
    zip: null,
    guid: null,
  },
];

var domain_url = "https://app-service-amworks.azurewebsites.net/";

const fetchApi = async () => {
  const response = await fetch(`${domain_url}core/api/test-building/`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
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
  console.log("new data", res);
  return res;
};
