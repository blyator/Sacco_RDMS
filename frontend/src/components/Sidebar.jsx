import React from 'react';
import { 
  Home, 
  UserPlus, 
  CreditCard, 
  Code, 
  History,
  X
} from 'lucide-react';

const Sidebar = ({ activeTab, setActiveTab, isSidebarOpen, setIsSidebarOpen }) => {
  return (
    <aside 
      className={`fixed inset-y-0 left-0 z-30 w-64 bg-base-100 shadow-xl flex flex-col border-r border-base-300 transform transition-transform duration-300 ease-in-out md:relative md:translate-x-0 ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'}`}
    >
      <div className="p-6 border-b border-base-300 flex items-center justify-between">
        <a className="flex items-center gap-3 text-2xl font-black tracking-tight text-base-content no-underline">
          SACCO<span className="text-accent">RDMS</span>
        </a>
        <button 
          className="btn btn-ghost btn-xs btn-square md:hidden"
          onClick={() => setIsSidebarOpen(false)}
        >
          <X className="w-5 h-5" />
        </button>
      </div>
      
      <nav className="flex-1 p-4">
        <ul className="menu menu-lg w-full rounded-box gap-2">
          <li>
            <a 
              onClick={() => setActiveTab('DASHBOARD')} 
              className={activeTab === 'DASHBOARD' ? 'active font-bold' : 'font-medium opacity-70 hover:opacity-100'}
            >
              <Home className="w-5 h-5" /> Dashboard
            </a>
          </li>
          <li>
            <a 
              onClick={() => setActiveTab('MEMBERS')} 
              className={activeTab === 'MEMBERS' ? 'active font-bold' : 'font-medium opacity-70 hover:opacity-100'}
            >
              <UserPlus className="w-5 h-5" /> Members
            </a>
          </li>
          <li>
            <a 
              onClick={() => setActiveTab('ACCOUNTS')} 
              className={activeTab === 'ACCOUNTS' ? 'active font-bold' : 'font-medium opacity-70 hover:opacity-100'}
            >
              <CreditCard className="w-5 h-5" /> Accounts
            </a>
          </li>
          <li>
            <a 
              onClick={() => setActiveTab('SQL')} 
              className={activeTab === 'SQL' ? 'active font-bold' : 'font-medium opacity-70 hover:opacity-100'}
            >
              <Code className="w-5 h-5" /> SQL Terminal
            </a>
          </li>
          <li>
            <a 
              onClick={() => setActiveTab('LOGS')} 
              className={activeTab === 'LOGS' ? 'active font-bold' : 'font-medium opacity-70 hover:opacity-100'}
            >
              <History className="w-5 h-5" /> System Logs
            </a>
          </li>
        </ul>
      </nav>

      <div className="p-4 bg-base-200 m-4 rounded-xl border border-base-300">
         <div className="text-[10px] opacity-50 font-black uppercase mb-1">Current User</div>
         <div className="font-bold text-sm">Admin</div>
      </div>
    </aside>
  );
};

export default Sidebar;
